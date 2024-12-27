"""1014. Best Sightseeing Pair"""


class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        # max=float('-inf')
        # for i in range(len(values)-1):
        #     for j in range(i+1,len(values)):
        #         if (values[i]+values[j]+i-j)>max:
        #             max=(values[i]+values[j]+i-j)

        # return max

        # i,j=0,1
        # max=float('-inf')
        # while i<len(values)-1:
        #     if (values[i]+values[j]+i-j)>max:
        #         max=(values[i]+values[j]+i-j)
        #     j+=1
        #     if j==len(values):
        #         i+=1
        #         j=i+1
        # return max

        max_i = values[0] + 0
        max_s = float('-inf')
        for i in range(1, len(values)):
            max_s = max(max_s, max_i + values[i] - i)
            max_i = max(max_i, values[i] + i)
        return max_s



