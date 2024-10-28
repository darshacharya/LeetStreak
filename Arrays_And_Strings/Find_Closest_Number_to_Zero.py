
"""Find Closest Number to Zero Approach : (1)"""
"""TC: O(n)"""
"""SC: O(1)"""
nums = [4,-2,4,2,-1,1]
target = nums[0]
for num in nums[1:]:
    if abs(num)<abs(target) or (abs(num)==abs(target) and num>target):
        target=num
print(target)



"""Find Closest Number to Zero Approach : (2)"""
"""TC: O(n)"""
"""SC: O(1)"""
def closest(nums):
    if not nums:  # O(1)
        return None

    # Initialize closest number as the first element
    closest = nums[0]

    # If the abs value of the current number is smaller, or if
    # the same but positive
    for num in nums[1:]:  # O(n), n = length of the list
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num

    return closest

print(closest(nums))