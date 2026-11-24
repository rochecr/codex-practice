import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "greet.py"


class GreetingTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True,
            text=True,
            timeout=5,
        )

    def test_greetings_and_flag_combinations(self):
        cases = [
            ([], "Hello, World!\n"),
            ([""], "Hello, !\n"),
            (["Rodrigo"], "Hello, Rodrigo!\n"),
            (["Maria Elena"], "Hello, Maria Elena!\n"),
            (["--uppercase"], "HELLO, WORLD!\n"),
            (["Maria Elena", "--uppercase"], "HELLO, MARIA ELENA!\n"),
            (["--goodbye"], "Goodbye, World!\n"),
            (["Rodrigo", "--repeat", "2"], "Hello, Rodrigo!\n" * 2),
            (
                ["Maria Elena", "--goodbye", "--uppercase", "--repeat", "2"],
                "GOODBYE, MARIA ELENA!\n" * 2,
            ),
        ]
        for args, expected in cases:
            with self.subTest(args=args):
                result = self.run_cli(*args)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, expected)
                self.assertEqual(result.stderr, "")

    def test_name_with_line_break_exits_with_status_two(self):
        for line_break in ("\n", "\r", "\r\n", "\u2028"):
            with self.subTest(line_break=line_break):
                result = self.run_cli(f"Maria{line_break}Elena", "--repeat", "2")
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn("name must not contain line breaks", result.stderr)

    def test_invalid_repeat_exits_with_status_two(self):
        for values in (["0"], ["-2"], ["2.5"], ["hello"], []):
            with self.subTest(values=values):
                result = self.run_cli("--repeat", *values)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn("argument --repeat:", result.stderr)

    def test_help_lists_options(self):
        result = self.run_cli("--help")
        self.assertEqual(result.returncode, 0, result.stderr)
        for option in ("--goodbye", "--uppercase", "--repeat"):
            self.assertIn(option, result.stdout)


if __name__ == "__main__":
    unittest.main()
