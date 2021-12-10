"""
The test for solution to doomsday fuel

Author: Christian M. Fulton
Date: 10.Dec.2021
"""
from solution import *

def test_solution():
    matrix = [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
        ]
    expected = [0, 3, 2, 9, 14]

    result = solution(matrix)
    assert expected == result