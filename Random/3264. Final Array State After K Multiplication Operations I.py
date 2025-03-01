"""3264. Final Array State After K Multiplication Operations I"""


def getFinalState(nums, k, multiplier):
    n = len(nums)
    for i in range(k):
        min_index = 0
        for j in range(n):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[min_index] *= multiplier


    return nums