"""167. Two Sum II - Input Array Is Sorted"""
"""TC: O(N)"""
"""SC: O(1)"""


def twoSum(numbers, target) :
    i,j=0,len(numbers)-1
    result=[]
    while i<j:
        if numbers[i]+numbers[j]==target:
            result.append(i+1)
            result.append(j+1)
            return result
        elif numbers[i]+numbers[j]>target:
            j-=1
        else:
            i+=1
