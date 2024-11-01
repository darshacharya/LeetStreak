"""56. Merge Intervals"""
"""TC:  O(n log n)"""
"""SC: O(n)"""
def merge(intervals):
    intervals.sort(key=lambda interval: interval[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]

    return merged

#example
intervals = [[1,2],[2,4]]
print(merge(intervals)) #[[1,4]]
