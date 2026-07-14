class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #contiguous subarray , bad approach
        # 2, 2+-3 , 2+-3 +4, 2+ -3 + 4 + -2,..... max Sum where
        maxSum = nums[0] 
        for i in range(len(nums)):
            cSum = 0  
            for j in range(i, len(nums)):
                cSum +=  nums[j]
                maxSum = max(maxSum, cSum)

        return maxSum
        

                
                