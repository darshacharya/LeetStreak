"""1957. Delete Characters to Make Fancy String"""
"""TC: O(n)"""
"""SC: O(n)"""

s = "aaabaaa"


def makeFancyString( s):
    result=s[:2]
    for char in s[2:]:
        if char == result[-1] and char==result[-2]:
            continue
        else:
            result+=char

    return result


print(makeFancyString(s))