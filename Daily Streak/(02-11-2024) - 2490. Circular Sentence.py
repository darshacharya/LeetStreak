"""TC: O(N)"""
"""SC: O(N) """

sentence = "leetcode exercises sound delightful"

def isCircularSentence(sentence):
    s = sentence.split()
    if s[0][0] != s[-1][-1]:
        return False
    else:
        for i in range(len(s) - 1):
            if s[i][-1] == s[i + 1][0]:
                continue
            else:
                return False
    return True

print(isCircularSentence(sentence))
