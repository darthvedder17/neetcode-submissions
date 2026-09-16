class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            k = l + (r-l)//2
            totalSum = 0
            for p in piles:
                totalSum += math.ceil(float(p) / k)
            if totalSum <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res
                
       