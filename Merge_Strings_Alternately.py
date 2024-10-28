"""Merge Strings Alternately Approach: (1)"""
"""TC: O(n+m)"""
"""SC: O(n+m)"""
word1 = "drhn"
a = list(word1) # converting string into list
word2 = "asa"
b = list(word2) # converting string into list
res = [] # an empty list for result
m = min(len(a),len(b)) # number of iteration for appending one letter from each list

for i in range(m):
    res.append(a[i])
    res.append(b[i])

if len(a)>len(b):
    x = a[m :] # rest of letters in list a
    res.append(''.join(x))
elif len(a)<len(b):
    x = b[m :] # rest of letters in list b
    res.append(''.join(x))

print(''.join(res))

"""Merge Strings Alternately Approch: (2)"""
"""TC: O(n+m)"""
"""SC: O(n+m)"""
def mergeAlternately(word1, word2):
    result = []

    # Iterate through the minimum length of both words
    for i in range(min(len(word1), len(word2))):
        result.append(word1[i])
        result.append(word2[i])

    # Add remaining characters from the longer string
    result.append(word1[i + 1:] if len(word1) > len(word2) else word2[i + 1:])

    return ''.join(result)

print(mergeAlternately(word1,word2))