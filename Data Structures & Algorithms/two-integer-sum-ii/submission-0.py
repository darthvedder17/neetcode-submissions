class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        l,r = 0, len(numbers)-1
        while l < r:
            numberSum = numbers[l] + numbers[r]
            if numberSum == target:
                return [l+1, r+1]
            elif numberSum < target:
                l+=1
            else:
                r-=1
        return []
                
        