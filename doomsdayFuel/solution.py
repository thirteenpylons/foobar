"""
Write a function solution(m) that takes an array of array of nonnegative ints 
representing how many times that state has gone to the next state and return an 
array of ints for each terminal state giving the exact probabilities of each 
terminal state, represented as the numerator for each state, then the 
denominator for all of them at the end and in simplest form. The matrix 
is at most 10 by 10. 

It is guaranteed that no matter which state the ore is in, 
there is a path from that state to a terminal state. That is, the processing 
will always eventually end in a stable state. 
The ore starts in state 0. The denominator will fit within a signed 32-bit 
integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
  [
    [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
    [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
    [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
    [0,0,0,0,0,0],  # s3 is terminal
    [0,0,0,0,0,0],  # s4 is terminal
    [0,0,0,0,0,0],  # s5 is terminal
  ]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].


Author: Christian M. Fulton
Date: 10.Dec.2021
"""
import numpy as np
import fractions as f


def standard_form(matrix):
    rows, columns = matrix.shape
    swaps = 0
    to_swap = []

    for i in range(rows):
        if not np.any(matrix[i]):
            matrix = np.row_stack((matrix[i], matrix))
            matrix = np.delete(matrix, i+1, 0)
            swaps += 1
        else:
            to_swap.append(i)
            matrix[i] /= matrix[i].sum()

    aux = matrix.copy()
    for counter, i in enumerate(to_swap):
        matrix = np.column_stack((matrix, aux[:, i]))
        matrix = np.delete(matrix, i-counter, 1)
    for i in range(swaps):
        matrix[i, i] = 1
    return matrix, swaps


def solution(m):
    states, swaps = standard_form(np.matrix(m, dtype=float))
    FR = states
    if len(states) > 1:
        Q = states[swaps:, swaps:]
        I = np.diag(np.ones(len(Q)))
        R = states[swaps:, :swaps]
        F = (I-Q)**(-1)
        FR = F*R

    result = map(f.Fraction, FR[0].A1.tolist())
    denominators = []
    for i in range(len(result)):
        result[i] = result[i].limit_denominator(100)
        denominators.append(result[i].denominator)
    lcm = np.lcm.reduce(denominators)
    numerators = [
        result[i].numerator * lcm / result[i].denominator
        for i in range(len(result))
    ]

    numerators.append(lcm)

    return numerators