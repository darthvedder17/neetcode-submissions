class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitsLength = len(digits)
        for i in range(digitsLength-1,-1,-1):
            if digits[i] < 9:
                digits[i]+=1
                return digits
            digits[i] = 0
        return [1] + [0] * digitsLength

            
            
        
        