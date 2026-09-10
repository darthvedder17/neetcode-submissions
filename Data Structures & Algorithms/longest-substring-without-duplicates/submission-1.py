class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        if not s:
            return 0
        maxL = -float('inf')
        for r in range(len(s)):
            while s[r] in seen:
               seen.remove(s[l])
               l+=1
            seen.add(s[r])
            maxL = max(maxL, r -l +1)
        return maxL
          