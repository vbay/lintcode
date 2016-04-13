public class Solution {
    /**
     * @param n: an integer
     * @return: a boolean which equals to true if the first player will win
     */
    public boolean firstWillWin(int n) {
        // write your code here
        int []dp = new int[n+1];

        return MemorySearch(n, dp);

    }
    boolean MemorySearch(int n, int []dp) { // 0 is empty, 1 is false, 2 is true
        if(dp[n] != 0) {
            if(dp[n] == 1)
                return false;
            else
                return true;
        }
        if(n <= 0) {
            dp[n] = 1;
        } else if(n == 1) {
            dp[n] = 2;
        } else if(n == 2) {
            dp[n] = 2;
        } else if(n == 3) {
            dp[n] = 1;
        } else {
            if((MemorySearch(n-2, dp) && MemorySearch(n-3, dp)) ||
                (MemorySearch(n-3, dp) && MemorySearch(n-4, dp) )) {
                dp[n] = 2;
            } else {
                dp[n] = 1;
            }
        }
        if(dp[n] == 2)
            return true;
        return false;
    }
}
