class Solution:
    # @param {int} n a positive integer
    # @param {int[]} primes the given prime list
    # @return {int} the nth super ugly number
    def nthSuperUglyNumber(self, n, primes):
        # Write your code here
        import heapq
        length = len(primes)
        times = [0] * length
        uglys = [1]
        minlist = [(primes[i] * uglys[times[i]], i) for i in xrange(len(times))]
        heapq.heapify(minlist)

        while len(uglys) < n:
            (umin, min_times) = heapq.heappop(minlist)
            times[min_times] += 1
            if umin != uglys[-1]:
                uglys.append(umin)
            heapq.heappush(minlist, (primes[min_times] * uglys[times[min_times]], min_times))

        return uglys[-1] 
