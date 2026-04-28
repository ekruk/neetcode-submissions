from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # make them both sets and compare?
        # sort them both?
        # loop through both, add to dictionary, compare dictionaries?

        if len(s) != len(t):
            return False

        dic = defaultdict(int)
        dic_2 = defaultdict(int)

        for i in range(len(s)):
            dic[s[i]] += 1
            dic_2[t[i]] += 1

        if dic == dic_2:
            return True
        return False 
