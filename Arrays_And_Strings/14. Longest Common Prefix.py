"""14. Longest Common Prefix"""
"""TC: O(n)"""
"""SC: O(1)"""
def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Start with the first string as the initial common prefix
    prefix = strs[0]

    # Compare with each string in the array
    for s in strs[1:]:
        # Trim the prefix until it matches the start of the string
        while not s.startswith(prefix):
            prefix = prefix[:-1]  # Reduce the prefix length
            if prefix == "":  # Early return if there's no common prefix
                return ""

    return prefix


"""14. Longest Common Prefix Approach (2)"""
"""TC: O(n+m)"""
"""SC: o(1)"""
def longestCommonPrefix(strs):
    if not strs:
        return ""  # Return empty string if the list is empty

    # Find the shortest string in the list
    check = min(strs, key=len)

    for i in range(len(check)):
        for word in strs:
            if word[i] != check[i]:
                return check[:i]  # Return common prefix up to this point

    return check  # All characters matched, return the shortest string