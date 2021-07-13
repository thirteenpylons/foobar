"""
Quantum antimatter fuel comes in small pellets, which is convenient 
since the many moving parts of the LAMBCHOP each need to be fed fuel 
one pellet at a time. However, minions dump pellets in bulk into the 
fuel intake. You need to figure out the most efficient way to sort 
and shift the pellets down to a single pellet at a time. 

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive 
energy released when a quantum antimatter pellet is cut in half, the 
safety controls will only allow this to happen if there is an even 
number of pellets)

Author: Christian M. Fulton
Date: 12/07/2021

"""

def solution(n):
    """
    solution(n) which takes a positive integer 
    as a string and returns the minimum number of operations needed to 
    transform the number of pellets to 1. The fuel intake control panel 
    can only display a number up to 309 digits long, so there won't ever 
    be more pellets than you can express in that many digits.

    For example:
    solution(4) returns 2: 4 -> 2 -> 1
    solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

    Parameter n: A positive integer
    Precondition: n is an integer represented as a string
    """
    n = int(n)
    result = 0

    while n != 1:
        if n % 2 == 0:
            n = n / 2
        elif n == 3 or (n + 1)& n > (n - 1) & (n - 2):
            n -= 1
        else:
            n += 1
        
        result += 1
    return result