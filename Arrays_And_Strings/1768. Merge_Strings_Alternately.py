# """Merge Strings Alternately Approach: (1)"""
# """TC: O(n+m)"""
# """SC: O(n+m)"""
# word1 = "drhn"
# a = list(word1) # converting string into list
# word2 = "asa"
# b = list(word2) # converting string into list
# res = [] # an empty list for result
# m = min(len(a),len(b)) # number of iteration for appending one letter from each list
#
# for i in range(m):
#     res.append(a[i])
#     res.append(b[i])
#
# if len(a)>len(b):
#     x = a[m :] # rest of letters in list a
#     res.append(''.join(x))
# elif len(a)<len(b):
#     x = b[m :] # rest of letters in list b
#     res.append(''.join(x))
#
# print(''.join(res))
#
# """Merge Strings Alternately Approch: (2)"""
# """TC: O(n+m)"""
# """SC: O(n+m)"""
# def mergeAlternately(word1, word2):
#     result = []
#
#     # Iterate through the minimum length of both words
#     for i in range(min(len(word1), len(word2))):
#         result.append(word1[i])
#         result.append(word2[i])
#
#     # Add remaining characters from the longer string
#     result.append(word1[i + 1:] if len(word1) > len(word2) else word2[i + 1:])
#
#     return ''.join(result)
#
# print(mergeAlternately(word1,word2))


def qualifying_score(input1, input2, input3, input4):
    # Step 1: Calculate the differences (S2[i] - S1[i])
    differences = [input4[i] - input3[i] for i in range(input1)]

    # Step 2: Sort the differences in descending order
    differences.sort(reverse=True)

    # Step 3: Sum the top P differences
    score = sum(differences[:input2])

    # Step 4: Check if score is greater than or equal to 35
    if score >= 35:
        return f"Qualified {score}"
    else:
        return f"Disqualified {score}"


# Example Usage:

# Example 1:
input1 = 5
input2 = 3
input3 = [5, 10, 15, 20, 25]
input4 = [15, 30, 20, 30, 25]
print(qualifying_score(input1, input2, input3, input4))  # Output: "Qualified 40"

# Example 2:
input1 = 6
input2 = 4
input3 = [6, 11, 36, 8, 24, 30]
input4 = [12, 11, 20, 10, 25, 30]
print(qualifying_score(input1, input2, input3, input4))  # Output: "Disqualified 9"