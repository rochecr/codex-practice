# Repository Guidelines

## Project Structure

- `greet.py` parses arguments and prints greetings using the Python standard library.
- `tests/test_greet.py` contains subprocess-based CLI tests.
- `README.md` covers usage and testing. `GITHUB_MCP_SETUP.md` covers GitHub MCP setup and troubleshooting.

Keep additions proportional to the project's size and introduce modules only when they improve clarity.

## Usage and Testing

Run commands from the repository root with Python 3. No installation or build step is required.

- `name` is optional and defaults to `World`. Quote names containing spaces.
- `--goodbye` changes the salutation from `Hello` to `Goodbye`.
- `--uppercase` uppercases the entire greeting.
- `--repeat N` prints the greeting on `N` lines. It defaults to one and requires a positive integer. Invalid values exit with status 2.
- `-h` or `--help` shows usage.

```bash
python3 greet.py
python3 greet.py "Maria Elena" --goodbye --uppercase --repeat 2
python3 greet.py --help
python3 -m unittest discover -s tests -v
```

Run the suite before submitting changes. Use descriptive test names and assert exact CLI output and exit status, including default behavior, combined flags, and invalid input.

## Coding Style

Use four-space indentation, descriptive `snake_case` names, top-level imports, and f-strings for simple interpolation. Prefer the standard library. No formatter or linter is configured.

## Commits and Pull Requests

Use `git log --oneline` to review existing commits. Follow the history's concise, imperative subjects, such as `Add goodbye greeting option`. Keep changes focused. In pull requests, describe the change, list validation commands and results, and link relevant issues when available. Include terminal output when useful.
