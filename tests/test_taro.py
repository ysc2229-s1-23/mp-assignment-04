import pytest
from questions.taro import taro_festival_happiness

@pytest.mark.parametrize("N, happiness, expected_output", [
    (3, [[10, 40, 70], [20, 50, 80], [30, 60, 90]], 210),
    (1, [[100, 10, 1]], 100),
    (7, [[6, 7, 8], [8, 8, 3], [2, 7, 2], [8, 10, 6], [4, 4, 10], [6, 6, 6], [5, 5, 8]], 55),
    (1, [[1, 0, 0]], 1),  
    (1, [[0, 1, 0]], 1),  
    (1, [[0, 0, 1]], 1),  
    (1, [[0, 0, 0]], 0),  

    (2, [[1, 0, 0], [0, 1, 0]], 2), 
    (2, [[0, 1, 0], [0, 0, 1]], 2), 

    (3, [[1, 2, 3], [6, 5, 4], [7, 8, 9]], 18), 
    (3, [[3, 2, 1], [4, 5, 6], [9, 8, 7]], 18), 

    (100, [[i, i+1, i+2] for i in range(1, 301, 3)], 15100), 
])
def test_taro_festival_happiness(N, happiness, expected_output):
    assert taro_festival_happiness(N, happiness) == expected_output
