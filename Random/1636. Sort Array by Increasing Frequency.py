"""1636. Sort Array by Increasing Frequency"""
"""TC: O(NLogN)"""
"""SC: O(N)"""


from itertools import count
from collections import  Counter
nums = [1,1,2,2,2,3]

def frequencySort(nums):
    count = Counter(nums)
    ans = sorted(nums, key=lambda x: (count[x], -x))
    return ans

print(frequencySort(nums))