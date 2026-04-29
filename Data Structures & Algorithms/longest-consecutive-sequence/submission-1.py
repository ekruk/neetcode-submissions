class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        new_nums = set(nums)
        longest = 0
        temp = 0

        for c in new_nums:
            if c - 1 not in new_nums:
                con = c
                temp = 1
                while (con + 1) in new_nums:
                    temp += 1
                    longest = max(temp, longest)
                    con += 1

        return max(longest, temp)
                    