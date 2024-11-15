"""1189. Maximum Number of Balloons"""


def maxNumberOfBalloons(text):
    counter = 0
    balloon = "balloon"

    for c in text:
        if c in balloon:
            counter[c] += 1

    if any(c not in counter for c in balloon):
        return 0
    else:
        return min(counter["b"], counter["a"], counter["l"] // 2, counter["o"] // 2, counter["n"])


