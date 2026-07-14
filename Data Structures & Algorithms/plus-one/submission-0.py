class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        combined = int("".join(map(str, digits)))
        return list(str(combined+1))
        