import pytest

from tennis import tennis_score


# Takes a list of params to pass in and then a list of all the test cases with values for each param
@pytest.mark.parametrize("p1_points, p2_points, expected_score",
                         [(0, 0, "Love-All"),
                          (1, 1, "Fifteen-All"),
                          (2, 2, "Thirty-All"),
                          (3, 3, "Fourty-All"),
                          ])
def test_score_tennis(p1_points, p2_points, expected_score):
    assert tennis_score(p1_points, p2_points) == expected_score


# def test_0_0_love_all():
#     assert tennis_score(0, 0) == "Love-All"
#
#
# def test_1_1_love_all():
#     assert tennis_score(1, 1) == "Fifteen-All"
#
#
# def test_2_2_love_all():
#     assert tennis_score(2, 2) == "Thirty-All"
