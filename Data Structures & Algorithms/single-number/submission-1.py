class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        # XOR is commutative and associative, order doesn't matter
        # a ^ a = 0 
        # a ^ 0 = a
        for n in nums:
            res ^= n
        return res
        