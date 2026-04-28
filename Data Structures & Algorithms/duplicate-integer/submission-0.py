class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set?
        # loop through with array with dictionary

        dic = {}
        
        for c in nums:
            if c not in dic:
                dic[c] = 1
            else:
                return True

        return False

        