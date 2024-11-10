"""771. Jewels and Stones"""
"""TC: O(N∗M)"""
"""SC: O(1)"""


def numJewelsInStones(jewels, stones) :
    count = 0
    for letter in stones:
        if letter in jewels:
            count += 1

    return count

# example
jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels,stones))