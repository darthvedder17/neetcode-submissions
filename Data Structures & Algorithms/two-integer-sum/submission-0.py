class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumDict = {}
        if not nums:
            return []
        for i, number in enumerate(nums):
            result = target - number
            if result in twoSumDict.keys():
                return [twoSumDict[result],i]
            else:
                twoSumDict[number] = i
        return []



# Dry Run :
# target = 7
# 3 ; result = 4 ; {3:0}
# 4 ; result = 3 ;  return []