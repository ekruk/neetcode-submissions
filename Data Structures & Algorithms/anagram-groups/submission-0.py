class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}

        for c in strs:
            c_sort = "".join(sorted(c))
            if dic.get(c_sort) is None:
                dic[c_sort] = [c]
            else:
                dic[c_sort].append(c)

        return list(dic.values())