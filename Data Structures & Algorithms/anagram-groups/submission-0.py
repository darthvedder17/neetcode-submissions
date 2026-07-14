class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = list(sorted(n) for n in strs)
        final_list = []
        ditto = {}
        for i in range(len(sorted_strs)):
            if tuple(sorted_strs[i]) not in ditto:
                ditto[tuple(sorted_strs[i])] = [strs[i]]
            else:
                ditto[tuple(sorted_strs[i])].append(strs[i])
        return list(v for v in ditto.values())
        
    