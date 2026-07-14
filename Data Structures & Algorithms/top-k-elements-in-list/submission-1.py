from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countedDict = Counter(nums)
        # {1:3,2:2,3:1}
        bucket = [[] for _ in range(len(nums)+1)]
        for idx,cnt in countedDict.items():
            bucket[cnt].append(idx)
        res = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res     
            
        