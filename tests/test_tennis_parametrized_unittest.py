import unittest
from tennis import tennis_score


# Parametrized tests
class TennisTest(unittest.TestCase):

    def test_tennis_score(self):
        test_cases = [
            (0, 0, "Love-All"),
            (1, 1, "Fifteen-All"),
            (2, 2, "Thirty-All"),
            (3, 3, "Fourty-All"),
        ]
        for p1_points, p2_points, expected_score in test_cases:
            # self.subTest is necessary, actually creates sub tests that you can see in test runner
            with self.subTest(f"This is a test for {expected_score}"):
                self.assertEqual(expected_score, tennis_score(p1_points, p2_points))
