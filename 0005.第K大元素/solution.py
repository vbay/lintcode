class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        A = sorted(A, reverse=True)
        return A[k-1]
