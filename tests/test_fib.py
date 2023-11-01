import pytest
from questions.fib import fibonacci

@pytest.mark.parametrize("input_val, expected_output", [
    (0, 0),
    (1, 1),
    (10, 55),
    (7, 13),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (100, 354224848179261915075),  # Testing large values to ensure O(n) behavior
    (1000, 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)
])
def test_fibonacci(input_val, expected_output):
    assert fibonacci(input_val) == expected_output
