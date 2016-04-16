public class Solution {
    /**
     * @param n: An integer
     * @return: An integer
     */
    public int climbStairs(int n) {
        // write your code here
        if (n <=1){
            return 1;
        }
        int last = 1, lastlast = 1;
        int now = 0;
        for (int i = 2;i <=n; i++){
            now = last +lastlast;
            lastlast = last;
            last = now;
        }
        return now;
    }
}
