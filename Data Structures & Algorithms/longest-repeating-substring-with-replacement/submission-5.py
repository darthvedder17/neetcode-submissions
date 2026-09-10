class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = -float('inf')
        l = 0
        countMap = dict() 
        maxF = 0
        res = 0
        for r in range(len(s)):
            countMap[s[r]]= 1 + countMap.get(s[r], 0)
            maxF = max(maxF, countMap[s[r]])
            # This means it's an invalid window, we must descrease the size 
            while (r-l+1) - maxF > k :
                countMap[s[l]] -=1
                l+=1
            res = max(res,r-l+1)
        return res