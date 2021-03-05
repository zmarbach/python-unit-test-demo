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
            with self.subTest(f"{p1_points}, {p2_points} ---> {expected_score}"):
                self.assertEqual(expected_score, tennis_score(p1_points, p2_points))
