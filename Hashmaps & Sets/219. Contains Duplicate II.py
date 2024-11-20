"""219. Contains Duplicate II"""

def containsNearbyDuplicate(nums, k):
    # i=0
    # j=1
    # for i in range(len(nums)-1):
    #     for j in range(i+1,len(nums)):
    #         if nums[i]==nums[j]:
    #             if abs(i-j)<=k:
    #                 return True
    # return False

    seen = {}
    for i, val in enumerate(nums):
        if val in seen and i - seen[val] <= k:
            return True
        else:
            seen[val] = i

    return False

nums = [1,2,3,1]
k=3
print(containsNearbyDuplicate(nums,k)) #True