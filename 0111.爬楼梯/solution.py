class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n <= 2:
            return n
        result=[1,2]
        for i in range(n-2):
            result.append(result[-2]+result[-1])
        return result[-1]
