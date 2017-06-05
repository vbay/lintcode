class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        result = 0
        f, g, f1, g1 = 0, 0, 0, 0
        for x in A:
            f1 = g + x
            g1 = max(f, g)
            g, f = g1, f1

        return max(f, g)
