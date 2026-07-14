from typing import Set
class Solution:
    def isHappy(self, n: int, seen = None) -> bool:
        if seen is None:
            seen = set()
        if n == 1:
            return True
        if n in seen:
            return False
        res = 0
        seen.add(n)
        repetitiveList = list(str(n))
        for r in repetitiveList:
            res+= int(r)**2
        return self.isHappy(res,seen)

            
