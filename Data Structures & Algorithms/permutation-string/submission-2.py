class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        counter_s1 = {}
        counter_s2 = {}

        for c in s1:
            counter_s1[c] = 1 + counter_s1.get(c, 0)

        for i in range(len(s1)):
            counter_s2[s2[i]] = 1 + counter_s2.get(s2[i], 0)

        l = 0

        for r in range(len(s1), len(s2)):

            if counter_s1 == counter_s2:
                return True

            counter_s2[s2[l]] -= 1

            if counter_s2[s2[l]] == 0:
                del counter_s2[s2[l]]

            l += 1

            counter_s2[s2[r]] = 1 + counter_s2.get(s2[r], 0)

        return counter_s1 == counter_s2