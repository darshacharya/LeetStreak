"""164. Maximum Gap"""
"""TC: O(N) """
"""SC: O(N)"""
nums = [3,6,9,1]

def maximumGap(nums):
    if len(nums) < 2:
        return 0

    hi, lo, ans = max(nums), min(nums), 0
    bsize = max(1, (hi - lo) // (len(nums) - 1))
    buckets = [[] for _ in range((hi - lo) // bsize + 1)]

    for n in nums:
        idx = (n - lo) // bsize
        buckets[idx].append(n)

    currhi = 0
    for b in buckets:
        if not b:
            continue
        prevhi = currhi if currhi else b[0]
        currlo = min(b)
        currhi = max(b)

        ans = max(ans, currlo - prevhi)

    return ans




print(maximumGap(nums))
