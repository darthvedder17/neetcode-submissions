class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 
        for n in nums:
            # something_weird_happens is a bit operation
            # If similar number XORs 
            res^=n
        return res         
            