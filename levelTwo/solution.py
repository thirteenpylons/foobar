import functools
def solution(xs):
    """
    
    """
    if len(xs) == 1:
        return str(xs[0])
    xs = [(n) for n in xs if n != 0] # store negative integers
    pos = [(n) for n in xs if n > 0] # store positive integers
    xs = [(n) for n in xs if n < 0] # keep neg int
    if len(xs) % 2 != 0: # check num of negs even or odd
        xs = sorted(xs)
        popped = xs.pop()

    resultList = xs + pos
    if len(pos) == 0 and len(xs) == 0:
        return str(0)
 
    result = functools.reduce(lambda x,y: x * y, resultList) 
    return str(result)