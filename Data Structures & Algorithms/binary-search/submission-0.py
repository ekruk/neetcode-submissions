class Solution:
    def search(self, nums: List[int], target: int) -> int:

        r = len(nums) - 1
        l = 0

        middle = l + ((r - l) // 2)

        while l <= r:
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        
            middle = l + ((r - l) // 2)

        return -1