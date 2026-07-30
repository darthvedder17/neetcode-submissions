class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import lru_cache
        @lru_cache()
        def numWays(i):
            if i == n :
                return 1
            if i > n :
                return 0
            return numWays(i+1) + numWays(i+2)
           
        return numWays(0)
        