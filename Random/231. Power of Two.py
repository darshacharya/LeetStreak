"""231. Power of Two"""
"""TC: O(logN)"""
"""SC:O(1)"""


def isPowerOfTwo(n):
    if n < 2:
        if n == 1:
            return True
        return False
    while n > 2:
        n = n / 2
    return n == 2


print(isPowerOfTwo(512))