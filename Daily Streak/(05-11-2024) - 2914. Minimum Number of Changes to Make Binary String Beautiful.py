"""2914. Minimum Number of Changes to Make Binary String Beautiful"""
"""TC: O(N)"""
"""SC: O(1)"""

def minChanges(self, s):
    cnt = 0
    i = 1
    while i < len(s):
        if s[i] != s[i - 1]:
            cnt += 1
        i += 2
    return cnt