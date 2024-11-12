"""217. Contains Duplicate"""
"""TC: """
"""SC: """


def containsDuplicate(nums):
    if len(nums) == len(set(nums)):
        return False
    return True