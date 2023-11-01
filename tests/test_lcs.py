import pytest
from solutions.lcs import longest_common_segment

@pytest.mark.parametrize("s, t, expected", [
    # Normal Cases
    ("abcdef", "acef", "acef"),
    ("abcdef", "azc", "ac"),
    ("agcft", "gct", "gct"),
    ("programming", "algorithm", "orm"),

    # Edge Cases
    ("a", "b", ""),
    ("a", "a", "a"),
    ("abcde", "", ""),
    ("", "abcde", ""),

    # Efficiency Tests
    ("a" * 1500 + "b" * 1500, "a" * 1500 + "c" * 1500, "a" * 1500),
    ("a" * 3000, "a" * 3000, "a" * 3000),
])
def test_longest_common_segment(s, t, expected):
    assert longest_common_segment(s, t) == expected
