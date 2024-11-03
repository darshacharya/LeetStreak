def rotateString(s, goal):
    """TC: O(N)"""
    # if s == goal:
    #     return True
    # if len(s)!=len(goal):
    #     return False
    # for i in range(len(s) - 1):
    #     temp = s[i:] + s[:i]
    #     if temp == goal:
    #         return True
    # return False

    """TC: O(N)"""
    if len(s)!=len(goal):
        return False
    return goal in s+s

s = "abc"
goal = "cab"
print(rotateString(s,goal))
