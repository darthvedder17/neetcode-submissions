class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        numsC = Counter(nums)
        for c in numsC.values():
            if c > 1:
                return True
        return False
        