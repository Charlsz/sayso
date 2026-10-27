#!/usr/bin/env python3
"""Validate the Sayso eval suite and score objective checks.

This does not call a model. With no run file, it checks that evals.json is
well formed and that the hand-written fixtures in fixtures.json separate a
known weak answer from a known better one. Those fixtures are not model output.

With a run file, it also scores saved answers for cases that define checks.
Pass or fail there is about those checks only. It is not a quality score and
it is not statistical significance.

Run from the repository root:

    python evals/check_suite.py
    python evals/check_suite.py evals/runs/some-run.json

A run file looks like this:

    {
      "date": "2026-10-28",
      "model": "name you can actually see",
      "settings": "temperature, or not exposed",
      "runs": 1,
      "with_sayso": {"case-slug": "the answer"},
      "without_sayso": {"case-slug": "the answer"}
    }
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EVALS_PATH = ROOT / "evals.json"
FIXTURES_PATH = ROOT / "fixtures.json"

REQUIRED = (
    "id",
    "slug",
    "suite",
    "category",
    "dimensions",
    "prompt",
    "expected_output",
    "constraints",
    "failure_modes",
    "assertions",
)

THEMES = (
    "naturalness",
    "voice",
    "professional_academic",
    "technical_accuracy",
    "scientific_uncertainty",
    "concision",
    "leave_unchanged",
    "code_review",
    "unsupported_claims",
    "explicit_instruction",
    "clarity",
    "adversarial",
)

# Cases written before the covers field. New cases carry covers themselves.
LEGACY_COVERS = {
    "dishwasher-film": ("naturalness", "concision"),
    "sister-text": ("voice",),
    "reschedule-interview": ("professional_academic", "explicit_instruction"),
    "norovirus-brief": ("scientific_uncertainty", "unsupported_claims"),
    "actigraphy-abstract": ("naturalness", "professional_academic", "scientific_uncertainty", "concision"),
    "retry-after-docs": ("technical_accuracy",),
    "password-reset-review": ("code_review",),
    "status-note": ("leave_unchanged", "concision"),
    "casual-message": ("voice", "naturalness", "explicit_instruction"),
    "preserve-voice": ("voice", "explicit_instruction"),
    "professor-email": ("professional_academic",),
    "precision-recall": ("technical_accuracy", "unsupported_claims"),
    "project-advice": ("unsupported_claims",),
    "process-thread": ("technical_accuracy", "concision"),
    "satellite-summary": ("scientific_uncertainty", "concision"),
    "get-user-review": ("code_review",),
    "leave-unchanged-message": ("leave_unchanged",),
    "flood-paragraph": ("scientific_uncertainty", "professional_academic"),
}


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def covers_for(case: dict) -> tuple[str, ...]:
    if case.get("covers"):
        return tuple(case["covers"])
    return LEGACY_COVERS.get(case["slug"], ())


def norm(text: str) -> str:
    return text.replace("\r\n", "\n").strip()


def folded(text: str) -> str:
    return norm(text).casefold()


def apply_check(output: str, check: dict) -> str | None:
    """Return a failure reason, or None when the check passes."""
    op = check["op"]
    raw = norm(output)
    low = folded(output)
    if op == "includes":
        if check["text"].casefold() not in low:
            return f"missing {check['text']!r}"
    elif op == "includes_exact" or op == "contains_exact":
        if check["text"] not in raw:
            return f"missing exact {check['text']!r}"
    elif op == "excludes":
        if check["text"].casefold() in low:
            return f"contains {check['text']!r}"
    elif op == "excludes_word":
        # A short forbidden word must not match inside another word.
        # "hey" is inside "They".
        word = re.escape(check["text"].casefold())
        if re.search(rf"(?<!\w){word}(?!\w)", low):
            return f"contains the word {check['text']!r}"
    elif op == "one_of":
        options = check["options"]
        if not any(option.casefold() in low for option in options):
            return f"none of {options!r}"
    elif op == "one_of_exact":
        options = check["options"]
        if not any(option in raw for option in options):
            return f"none of the exact options {options!r}"
    elif op == "max_added_chars":
        anchor = check["anchor"]
        allowed = len(anchor) + int(check["n"])
        if len(raw) > allowed:
            return f"length {len(raw)} exceeds {allowed}"
    else:
        return f"unknown check {op!r}"
    return None


def score(output: str, checks: list[dict]) -> list[str]:
    failures = []
    for check in checks:
        reason = apply_check(output, check)
        if reason:
            failures.append(reason)
    return failures


def validate_suite(data: dict) -> list[str]:
    errors = []
    cases = data.get("evals")
    if not isinstance(cases, list) or not cases:
        return ["evals.json has no cases"]
    seen_ids = set()
    seen_slugs = set()
    covered = set()
    for case in cases:
        slug = case.get("slug", "<missing slug>")
        for field in REQUIRED:
            if field not in case or case[field] in ("", [], None):
                errors.append(f"{slug}: missing {field}")
        if case.get("id") in seen_ids:
            errors.append(f"{slug}: duplicate id {case.get('id')}")
        seen_ids.add(case.get("id"))
        if slug in seen_slugs:
            errors.append(f"{slug}: duplicate slug")
        seen_slugs.add(slug)
        themes = covers_for(case)
        if not themes:
            errors.append(f"{slug}: no theme coverage")
        unknown = [theme for theme in themes if theme not in THEMES]
        if unknown:
            errors.append(f"{slug}: unknown themes {unknown}")
        covered.update(themes)
        for check in case.get("checks", []):
            if "op" not in check:
                errors.append(f"{slug}: a check has no op")
    missing = [theme for theme in THEMES if theme not in covered]
    if missing:
        errors.append(f"uncovered themes: {', '.join(missing)}")
    return errors


def check_fixtures(cases: list[dict], fixtures: dict) -> list[str]:
    errors = []
    fixture_cases = fixtures.get("cases", {})
    for case in cases:
        checks = case.get("checks")
        if not checks:
            continue
        slug = case["slug"]
        pair = fixture_cases.get(slug)
        if not pair or "weak" not in pair or "better" not in pair:
            errors.append(f"{slug}: fixture missing weak and better")
            continue
        weak_failures = score(pair["weak"], checks)
        better_failures = score(pair["better"], checks)
        if not weak_failures:
            errors.append(f"{slug}: weak fixture passed; the check does not catch it")
        if better_failures:
            errors.append(f"{slug}: better fixture failed: {'; '.join(better_failures)}")
    extra = sorted(set(fixture_cases) - {case["slug"] for case in cases if case.get("checks")})
    if extra:
        errors.append(f"fixtures with no checks: {', '.join(extra)}")
    return errors


def score_run(cases: list[dict], run: dict) -> tuple[list[str], list[str], int]:
    lines = []
    problems = []
    scored = 0
    for label in ("with_sayso", "without_sayso"):
        answers = run.get(label)
        if not isinstance(answers, dict):
            problems.append(f"run file missing object {label}")
            continue
        for case in cases:
            checks = case.get("checks")
            if not checks:
                continue
            slug = case["slug"]
            if slug not in answers:
                lines.append(f"{label} {slug}: no answer saved")
                continue
            scored += 1
            failures = score(answers[slug], checks)
            if failures:
                problems.append(f"{label} {slug}: {'; '.join(failures)}")
                lines.append(f"{label} {slug}: fail ({'; '.join(failures)})")
            else:
                lines.append(f"{label} {slug}: pass")
    return lines, problems, scored


def main(argv: list[str]) -> int:
    data = load_json(EVALS_PATH)
    fixtures = load_json(FIXTURES_PATH)
    errors = validate_suite(data)
    errors.extend(check_fixtures(data["evals"], fixtures))
    checked = sum(1 for case in data["evals"] if case.get("checks"))
    print(f"Suite: {len(data['evals'])} cases, {checked} with objective checks")
    if errors:
        print("Failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Fixtures: each weak answer failed at least one check, and each better answer passed.")
    print("That only shows the checks can tell those hand-written answers apart.")
    if len(argv) == 1:
        print("Model comparison: not provided. No model was called.")
        return 0
    if len(argv) != 2:
        print("Usage: python evals/check_suite.py [run.json]")
        return 2
    run = load_json(Path(argv[1]))
    lines, problems, scored = score_run(data["evals"], run)
    print(f"Run file: {argv[1]}")
    print(f"Model: {run.get('model', 'not recorded')}; settings: {run.get('settings', 'not recorded')}; runs: {run.get('runs', 'not recorded')}")
    for line in lines:
        print(line)
    if problems:
        print("Objective checks failed. This is not a quality score.")
        return 1
    if scored == 0:
        print("No saved answers matched a case with objective checks.")
        return 0
    print("Objective checks passed for the saved answers. Human assertions are still separate, and one file is not a repeated result.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
