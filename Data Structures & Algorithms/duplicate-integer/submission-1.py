class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set?
        # loop through with array with dictionary

        new_set = set(nums)

        if len(new_set) != len(nums):
            return True
        return False
        