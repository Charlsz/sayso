# Technical documentation

Read this when documenting an API, command, configuration, or other interface.

The standard is that a caller can use the thing correctly without reading its implementation.

- Document the behavior you were given. If something is unspecified, say so or leave it out. Do not invent retries, units, defaults, or error types.
- Lead with what it does, then the inputs, the outputs, the edge cases, and a short example when an example makes the contract easier to apply.
- Use a signature, table, or list when the caller needs to look a field up. Use a sentence when the behavior is one rule.
- Say what the interface does not do when a reasonable caller would assume that it does.
- Keep terms consistent with the names in the interface. Do not rename a parameter for style.
