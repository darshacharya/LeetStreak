"""4. Median of Two Sorted Arrays"""

def findMedianSortedArrays(nums1,nums2):
    """TC: (O(m+n)*log(m+n))"""
    l = nums1+nums2
    l.sort()
    n =  len(l)
    if n%2:
        return l[n//2]
    else:
        mids = l[n//2] + l[(n//2)-1]
        return mids/2

def findMedianSortedArrays_(nums1, nums2):
    """TC: O(log(min(m, n)))"""
    n1 = len(nums1)
    n2 = len(nums2)

    # Ensure nums1 is the smaller array for simplicity
    if n1 > n2:
        return findMedianSortedArrays(nums2, nums1)

    n = n1 + n2
    left = (n1 + n2 + 1) // 2 # Calculate the left partition size
    low = 0
    high = n1

    while low <= high:
        mid1 = (low + high) // 2 # Calculate mid index for nums1
        mid2 = left - mid1 # Calculate mid index for nums2

        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')

        # Determine values of l1, l2, r1, and r2
        if mid1 < n1:
            r1 = nums1[mid1]
        if mid2 < n2:
            r2 = nums2[mid2]
        if mid1 - 1 >= 0:
            l1 = nums1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = nums2[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            # The partition is correct, we found the median
            if n % 2 == 1:
                return max(l1, l2)
            else:
                return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            # Move towards the left side of nums1
            high = mid1 - 1
        else:
            # Move towards the right side of nums1
            low = mid1 + 1
    return 0 # If the code reaches here, the input arrays were not sorted.


from statistics import median
def findMedianSortedArrays__(nums1, nums2):
    """TC: (O(m+n)*log(m+n))"""
    return median(sorted(nums1 + nums2))

nums1 = [1,2]
nums2 = [3,4]
nums3 = [1,3]
nums4 = [2]
print(findMedianSortedArrays(nums1,nums2))
print(findMedianSortedArrays(nums3,nums4))
print(findMedianSortedArrays_(nums1,nums2))
print(findMedianSortedArrays_(nums3,nums4))
print(findMedianSortedArrays__(nums1,nums2))
print(findMedianSortedArrays__(nums3,nums4))
