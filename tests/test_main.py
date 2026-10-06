import unittest
import subprocess
import sys
from pathlib import Path

from main import calculate_stats


class StatsTests(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(
            calculate_stats([2, 4, 6]), {"count": 3, "total": 12, "average": 4}
        )

    def test_negative_numbers(self):
        self.assertEqual(calculate_stats([-2, -4])["average"], -3)

    def test_single_number(self):
        self.assertEqual(calculate_stats([7])["average"], 7)

    def test_empty_input(self):
        with self.assertRaisesRegex(ValueError, "пустым"):
            calculate_stats([])

    def test_nonfinite_input(self):
        for number in (float("nan"), float("inf"), -float("inf")):
            with self.subTest(number=number):
                with self.assertRaisesRegex(ValueError, "конечными"):
                    calculate_stats([number])

    def test_fractional_numbers(self):
        self.assertAlmostEqual(calculate_stats([0.1, 0.2])["average"], 0.15)

    def test_cli_valid(self):
        result = self.cli("2", "4", "6")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Количество: 3\nСумма: 12\nСреднее: 4\n")

    def test_cli_invalid(self):
        for args in [(), ("abc",), ("nan",), ("inf",)]:
            with self.subTest(args=args):
                result = self.cli(*args)
                self.assertEqual(result.returncode, 2)
                self.assertIn("error:", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    @staticmethod
    def cli(*args):
        return subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parents[1] / "main.py"), *args],
            capture_output=True, text=True,
        )


if __name__ == "__main__":
    unittest.main()
