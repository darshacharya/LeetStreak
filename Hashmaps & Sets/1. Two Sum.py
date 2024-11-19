"""1. Two Sum"""
"""TC: O(N)"""
"""SC: O(N)"""

def twoSum(nums, target):
    prevmap = {}
    for i,n in enumerate(nums):
        diff = target-n
        if diff in prevmap:
            return [prevmap[diff],i]
        prevmap[n]=i

nums = [2,7,11,15]
target = 9

print(twoSum(nums,target))