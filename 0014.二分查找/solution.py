class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        index = 0
        for num in nums:
            if num == target:
                return index
            index += 1
        return -1
