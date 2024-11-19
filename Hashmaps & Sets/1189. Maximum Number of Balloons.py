"""1189. Maximum Number of Balloons"""
from collections import defaultdict


def maxNumberOfBalloons(text):
    counter = defaultdict(int)
    balloon = "balloon"

    for c in text:
        if c in balloon:
            counter[c] += 1

    if any(c not in counter for c in balloon):
        return 0
    else:
        return min(counter["b"], counter["a"], counter["l"] // 2, counter["o"] // 2, counter["n"])


print(maxNumberOfBalloons("banndjakloabaonsballons")) #1