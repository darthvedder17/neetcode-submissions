class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import lru_cache
        @lru_cache() 
        def dfs(i):
            if i == n:
                return 1
            if i > n :
                return 0
            return dfs(i+1) + dfs(i+2)
        return dfs(0) 
        