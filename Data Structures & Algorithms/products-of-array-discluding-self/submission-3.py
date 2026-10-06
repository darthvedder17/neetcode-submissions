class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # prefixArr = [1] * n
        # suffixArr = [1] * n
        prefix = 1
        res = [1] * n
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            # prefixArr[i] = prefixArr[i-1] * nums[i-1]
        postfix = 1
        for j in range(n-1,-1,-1):
            res[j] *= postfix
            postfix *= nums[j]
            # suffixArr[j] = suffixArr[j+1] * nums[j+1]
        # for i in range(n):
        #     res[i] = prefixArr[i] * suffixArr[i]
        return res
        

                    
        
            
        