class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # make them both sets and compare?
        # sort them both?
        # loop through both, add to dictionary, compare dictionaries?

        new_s = sorted(s)
        new_t = sorted(t)

        if new_s == new_t:
            return True
        return False