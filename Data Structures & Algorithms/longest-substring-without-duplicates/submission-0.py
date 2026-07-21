class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        g_max = 0
        l,r = 0,0
        seen = set()
        while r< len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            g_max = max(g_max,r-l+1)
            r+=1
        return g_max
        