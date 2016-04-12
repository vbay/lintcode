class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        return source.find(target)
