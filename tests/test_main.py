import unittest

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


if __name__ == "__main__":
    unittest.main()
