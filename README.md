# Codex Practice

Hands-on exercises with Python CLI development, Git, GitHub, and Codex MCP.

This small project demonstrates argument parsing, input validation, command-line testing, and documenting a tool integration.

## Run the greeting program

Python 3 is required. No dependencies or installation step are needed. From the repository root:

```bash
python3 greet.py
# Hello, World!

python3 greet.py Rodrigo
# Hello, Rodrigo!

python3 greet.py "Maria Elena" --goodbye --uppercase --repeat 2
# GOODBYE, MARIA ELENA!
# GOODBYE, MARIA ELENA!

python3 greet.py --help
```

| Argument | Behavior |
| --- | --- |
| `name` | Optional name; defaults to `World`. Quote names containing spaces. |
| `--goodbye` | Use `Goodbye` instead of `Hello`. |
| `--uppercase` | Uppercase the entire greeting. |
| `--repeat N` | Print the greeting `N` times; defaults to `1`. Requires a positive integer. |

Invalid repeat values, such as `0`, `-2`, `2.5`, `hello`, or a missing value, produce an error and exit status `2`.

## Run tests

The tests use Python's standard-library `unittest` and run the program as a subprocess to check its output and exit status:

```bash
python3 -m unittest discover -s tests -v
```

## Repository contents

- `greet.py`: greeting command-line program.
- `tests/test_greet.py`: CLI regression tests.
- [GITHUB_MCP_SETUP.md](GITHUB_MCP_SETUP.md): GitHub MCP setup, token handling, and Codex background-server troubleshooting.
- [AGENTS.md](AGENTS.md): contributor guidance from the initial exercise.

## Working with GitHub MCP

MCP lets Codex use GitHub tools to inspect repositories, issues, and pull requests. Git handles local commits and pushes. Follow the setup guide, then start with a read-only request such as: `Show my GitHub profile.`

Keep personal access tokens outside this repository. The setup guide uses an environment variable and contains no credentials.
