class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)
        longest = 0 

        for n in numSet:
            if (n-1) not in numSet:
                l = 1
                while (n + l) in numSet:
                    l+=1
                longest = max(l,longest)
        return longest