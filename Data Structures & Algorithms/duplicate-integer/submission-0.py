class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

        # (1,2,3) > [1,2,3,3] False
         