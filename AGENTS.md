# Repository Guidelines

## Project Structure & Module Organization

This project is a small Python command-line greeting program. `greet.py` at the repository root contains argument parsing and greeting output. It accepts an optional name and a `--uppercase` flag. There are currently no test directories, assets, package metadata, or third-party dependencies. Keep additions proportional to this scope; introduce separate modules only when they improve clarity.

## Build, Test, and Development Commands

Run commands from the repository root using Python 3. No build or installation step is required.

```bash
python3 greet.py                         # Hello, World!
python3 greet.py Rodrigo                 # Hello, Rodrigo!
python3 greet.py "Maria Elena"           # Hello, Maria Elena!
python3 greet.py --uppercase             # HELLO, WORLD!
python3 greet.py Rodrigo --uppercase     # HELLO, RODRIGO!
python3 greet.py --help                  # Show supported arguments
```

Quote names containing spaces so the shell passes them as one argument.

## Coding Style & Naming Conventions

Follow standard Python conventions: four spaces for indentation, `snake_case` for variables and functions, and descriptive names. Keep imports at the top and use f-strings for simple interpolation. Prefer the standard library and preserve the small implementation. No formatter or linter is currently configured; do not document tool commands as available until configuration is added.

## Testing Guidelines

No automated testing framework or coverage threshold is configured. Before submitting changes, run the examples above and check their exact output. Also verify a multiword name with `--uppercase`. Existing greetings must remain unchanged when the flag is absent, and the flag must uppercase the entire greeting. If automated tests become necessary, use descriptive names such as `test_default_greeting` and verify observable command-line output and exit status.

## Commit & Pull Request Guidelines

Git history is unavailable in this checkout, so no existing commit convention can be established. Use concise, imperative commit subjects, such as `Add uppercase greeting option`. Keep changes focused. Pull requests should describe the behavior changed and list validation commands and results. Link relevant issues when available. Screenshots are unnecessary for this command-line program; include terminal output when useful.
