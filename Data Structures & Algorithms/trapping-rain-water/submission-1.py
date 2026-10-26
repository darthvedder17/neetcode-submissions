class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        leftMx = [0] * n 
        rightMx = [0] * n
        leftMx[0] = height[0]

        for i in range(1,n):
            leftMx[i] = max(leftMx[i-1], height[i])
        rightMx[n-1] = height[n-1]

        for i in range(n-2,-1,-1):
            rightMx[i] = max(rightMx[i+1], height[i])

        res = 0 
        for i in range(n):
            res += min(leftMx[i], rightMx[i]) - height[i]
        return res
    