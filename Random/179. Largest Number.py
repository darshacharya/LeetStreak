"""179. Largest Number"""
"""TC: O(NLogN)"""
"""SC: O(N)"""

nums = [10,2]
def largenum(nums):
    # Convert integers to strings
    array = list(map(str, nums))

    # Custom sorting with a lambda function
    array.sort(key=lambda x: x * 10, reverse=True)

    # Handle the case where the largest number is "0"
    if array[0] == "0":
        return "0"

    # Build the largest number from the sorted array
    largest = ''.join(array)

    return largest

print(largenum(nums))
