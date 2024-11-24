"""35. Search Insert Position"""
"""TC :O(log N)"""
"""SC: O(1)"""

def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left

nums = [1,2,3,5]
target = 4
print(searchInsert(nums,target))