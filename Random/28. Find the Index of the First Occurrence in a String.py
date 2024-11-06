
haystack = "sadbutsad"
needle = "sad"

def strStr(haystack: str, needle: str):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

print(strStr(haystack,needle))