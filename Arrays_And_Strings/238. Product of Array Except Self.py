"""238. Product of Array Except Self"""
"""TC: O(n^2)"""
"""SC: O(1)"""

nums = [1,2,3,4]
def productExceptSelf(nums):
    i=0
    result = []

    while i< len(nums):
        temp = 1
        for j in range(len(nums)):
            if nums[j]==nums[i]:
                continue
            else:
                temp*=nums[j]
        result.append(temp)
        i+=1
    return result
print(productExceptSelf(nums))


"""Optimal solution"""
"""TC: O(n)"""
"""SC: O(1)"""
def product_ExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    # Step 1: Calculate prefix products and store in result
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Step 2: Calculate suffix products and multiply with result
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

print(product_ExceptSelf(nums))



