class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for num in nums:
            if num not in myDict.keys():
                myDict[num] = 1
            else:
                myDict[num]+=1
        # sortedDict = {k:v for k,v in sorted(myDict.items(), reverse=True)}
        sortedDict = sorted(myDict.items(), key =lambda x:x[1],reverse=True)
        res = [] 
        print(sortedDict)
        for k,v in sortedDict[:k]:
            res.append(k) 
        return res 
            
        