"""169. Majority Element"""


def majorityElement(nums):
    hash = {}
    res = majority = 0

    for n in nums:
        hash[n] = 1 + hash.get(n, 0)
        if hash[n] > majority:
            res = n
            majority = hash[n]

    return res

