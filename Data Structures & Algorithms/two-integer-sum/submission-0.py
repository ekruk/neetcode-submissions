class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}

        for i in range(len(nums)):
            if dic.get(target - nums[i]) is not None:
                return [dic.get(target - nums[i]), i]

            if nums[i] not in dic:
                dic[nums[i]] = i
            
        
        