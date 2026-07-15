class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for n in range(len(nums)):
            mul = 1 
            i = 0 
            while i < len(nums):
                if i!=n:
                    mul *= nums[i]
                i+=1
            res.append(mul)
        return res
                
        

        