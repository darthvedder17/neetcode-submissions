class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        freqCounter = {}
        l = 0
        maxFreq = 0
        for r in range(len(s)):
            freqCounter[s[r]] = 1 + freqCounter.get(s[r], 0)
            maxFreq = max(maxFreq, freqCounter[s[r]])

            while (r-l+1) - maxFreq > k:
                freqCounter[s[l]] -=1
                l+=1
            maxLength = max(maxLength, r-l+1)
        return maxLength
                 
        