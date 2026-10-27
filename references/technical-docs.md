# Technical documentation

Read this when documenting an API, command, configuration, or other interface.

The job is that a caller with the error in front of them can find what the interface does and what they must not assume. They should not need the implementation.

- Document the behavior you were given. If something is unspecified, say so or leave it out. Do not invent retries, units, defaults, or error types.
- Lead with what it does, then the inputs, the outputs, the edge cases, and a short example when an example makes the contract easier to apply.
- Use a signature, table, or list when the caller needs to look a field up. Use a sentence when the behavior is one rule.
- Say what the interface does not do when a reasonable caller would assume that it does.
- Keep terms consistent with the names in the interface. Do not rename a parameter for style.
