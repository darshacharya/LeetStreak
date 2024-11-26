
def sortedSquares(nums):
    """ Time: O(n log n) """
    """ Space: O(1) """
    # n = len(nums)
    # for i in range(n):
    #     nums[i] = nums[i] ** 2

    # nums.sort()

    # return nums

    """Time: O(n)"""
    """Space: O(n)"""
    n = len(nums)
    L, R = 0, n - 1
    result = []

    for i in range(n):
        nums[i] = nums[i] ** 2

    while L <= R:
        if nums[L] > nums[R]:
            result.append(nums[L])
            L += 1
        else:
            result.append(nums[R])
            R -= 1

    result.reverse()
    return result