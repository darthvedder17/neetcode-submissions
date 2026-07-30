class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target = (n * (n+1))//2
        for n in nums:
            target -= n
        return target if target >= 0 else -1
 
        