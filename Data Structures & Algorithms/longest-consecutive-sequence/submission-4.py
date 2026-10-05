class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        # current = nums[0]
        maxLength = 0
        if not nums:
            return 0
        for num in numSet:
            if (num - 1) not in numSet:
                currLength = 1
                while (num + currLength) in numSet:
                    currLength += 1
                maxLength = max(maxLength, currLength)
        return maxLength 
        