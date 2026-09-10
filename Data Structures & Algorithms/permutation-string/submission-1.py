class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])
        l = 0
        for r in range(len(s1),len(s2)):
            if  s1_counter == s2_counter:
                return True
            
            s2_counter[s2[l]] -=1
            l+=1
            s2_counter[s2[r]] = 1 + s2_counter.get(s2[r], 0)
        return s1_counter == s2_counter        
            
        