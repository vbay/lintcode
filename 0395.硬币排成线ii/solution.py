class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        n, total = len(values), 0
        sumv, f = [], []
        if n<3: return True
        for i in xrange(n): total += values[i]
        for i in xrange(n):
            sumv.append(total)
            total -= values[i]
        f.append(sumv[n-1])
        f.append(sumv[n-2])
        for i in xrange(n-3, -1, -1):
            f.append(max(values[i]+(sumv[i+1]-f[n-1-i-1]), values[i]+values[i+1]+(sumv[i+2]-f[n-1-i-2])))
        if f[n-1]<sumv[0]-f[n-1]: return False
        else: return True
