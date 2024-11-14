"""242. Valid Anagram"""


s = "anagram"
t = "nagaram"


def isAnagram(s, t):
    """TC: O(n log n)"""
    """SC: O(n)"""
    # return sorted(s)==sorted(t)

    """TC: O(n)"""
    """SC: O(n)"""
    # return Counter(s)==Counter(t)

    """TC: O(n)"""
    """SC: O(n)"""
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True
