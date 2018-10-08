#!/usr/bin/python

'''69. Sqrt(x)'''
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    import math
    eps = 0.00001
    up = x * 1.
    down = x / 2.
    diff = down * down - x
    while abs(diff) > eps:
        if down * down > x:
            up = down
            down /= 2.
        else:
            down = (up + down) / 2.
        diff = down * down - x
    res = int(down)
    if abs(down - math.ceil(down)) < eps:
        res = int(math.ceil(down))
    return res

print(mySqrt(36))
print(mySqrt(2147395599))