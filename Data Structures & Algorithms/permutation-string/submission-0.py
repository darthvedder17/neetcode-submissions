class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        window_len = len(s1)
        for i in range(len(s2)):
            substring = s2[i:i+window_len]
            if sorted(substring) == sorted(s1):
                return True
        return False
            
        