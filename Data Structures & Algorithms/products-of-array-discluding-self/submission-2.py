class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixArr = [1] * n
        suffixArr = [1] * n
        for i in range(1,n):
            prefixArr[i] = prefixArr[i-1] * nums[i-1]

        for j in range(n-2,-1,-1):
            suffixArr[j] = suffixArr[j+1] * nums[j+1]
        res = [1] * n
        for i in range(n):
            res[i] = prefixArr[i] * suffixArr[i]
        return res
        

                    
        
            
        