import pytest
from questions.robots import robot_jump

@pytest.mark.parametrize("N, h, expected_output", [
    # Base test cases
    (4, [10, 30, 40, 20], 30),
    (2, [10, 10], 0),
    (6, [30, 10, 60, 10, 60, 50], 40),

    # Edge test cases
    (1, [1], 0),
    (2, [1, 1000000000], 999999999),
    (10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0),

    (5, [1, 100, 1, 100, 1], 0),
    (5, [1, 3, 7, 5, 10], 9),

    (6, [10, 20, 40, 70, 110, 160], 150),

    (6, [1, 100, 1, 1, 1, 100], 99),

    (6, [10, 12, 10, 12, 10, 12], 2),

    (6, [100, 70, 50, 35, 25, 10], 90),

    (7, [1, 100, 1, 100, 1, 100, 1], 0),

    (100, [i for i in range(1, 101)], 99),
])
def test_robot_jump(N, h, expected_output):
    assert robot_jump(N, h) == expected_output
