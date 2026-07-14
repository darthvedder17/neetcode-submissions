class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        longest = 0

        for n in nums:
            cur, curL = n , 0
            while cur in numSet:
                cur +=1
                curL +=1
            longest = max(longest, curL)
        return longest
            