"""Is subsequence Approach: (1)"""
"""TC: O(n + m)"""
"""SC: O(1)"""
s = "abcc"
t = "ahsbsicc"
def is_subsequence(s, t):
    i, j = 0, 0

    # Iterate while there are characters left in both strings
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            # If characters match, move both pointers forward
            i += 1
        # Move the pointer for string t forward in all cases
        j += 1

    # Check if all characters of s were matched
    return i == len(s)

print(is_subsequence(s, t))  # Output: True



"""Is subsequence Approach: (2)"""
"""TC: O(m) m is len of t string"""
"""SC: O(1)"""
def isSubsequence( s, t):
    S = len(s)
    T = len(t)
    if s == '': return True
    if S > T: return False

    j = 0
    for i in range(T):
        if t[i] == s[j]:
            if j == S - 1:
                return True
            j += 1

    return False

print(isSubsequence(s,t))



"""own approach"""
"""TC: O(n + m)"""
"""SC: O(1)"""
s = "abcc"
t = "ahsbsicc"
result = ""
i,j=0,0
while i<len(s) and j<len(t):
    if s[i]==t[j]:
        result+=t[j]
        i+=1
        j+=1
    else:
        j+=1
if result==s:
    print("true")
else:
    print("false")




