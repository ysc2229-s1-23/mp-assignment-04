import pytest
from solutions.randomness import probability_more_ones

@pytest.mark.parametrize(
    "N, probabilities, expected",
    [
        (3, [0.3, 0.6, 0.8], 0.612),
        (1, [0.5], 0.5),
        (5, [0.1, 0.2, 0.3, 0.4, 0.5], 0.15),
        (3, [0.1, 0.5, 0.9], 0.5),
        (7, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7], 0.27222),
        (9, [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1], 0.5),

        # Edge cases
        (1, [0.0], 0.0),
        (1, [1.0], 1.0),
        (3, [0.0, 0.0, 0.0], 0.0),
        (3, [1.0, 1.0, 1.0], 1.0),

        # Efficiency test
        (99, [0.5 for _ in range(99)], None),
    ]
)
def test_probability_more_ones(N, probabilities, expected):
    if expected is not None:
        assert abs(probability_more_ones(N, probabilities) - expected) < 1e-9
    else:
        assert probability_more_ones(N, probabilities) is not None
