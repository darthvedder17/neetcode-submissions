class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # racecar carrace
        return sorted(s) == sorted(t)
