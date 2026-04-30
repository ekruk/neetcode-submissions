class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        final = []
        check_set = set()

        for i in range(len(nums)):

            x = nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                
                if (x + nums[l] + nums[r] < 0):
                    l += 1
                
                elif (x + nums[l] + nums[r] > 0):
                    r -= 1

                else:
                    if (x, nums[l], nums[r]) not in check_set:
                        final.append([x, nums[l], nums[r]])
                        check_set.add((x, nums[l], nums[r]))
                    l += 1
                    r -= 1

        return final
                




        