class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        # Write your code here
        n = len(nums)
        for i in xrange(1, n):
            if i % 2 == 1 and nums[i] < nums[i - 1] or \
                i % 2 == 0 and nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i- 1], nums[i]
