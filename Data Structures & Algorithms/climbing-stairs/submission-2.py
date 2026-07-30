class Solution:
    def climbStairs(self, n: int) -> int:
        last,slast = 1, 1
        for _ in range(n-1):
            temp = slast
            slast += last
            last = temp
        return slast
        