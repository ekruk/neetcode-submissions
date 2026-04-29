class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        product = [0] * len(nums)

        for i in range(len(nums)):

            if i > 0:
                prefix[i] = nums[i] * prefix[i - 1]
            else:
                prefix[i] = nums[i]

        for i in range(len(nums) - 1, -1, -1):

            if i < len(nums) - 1:
                postfix[i] = nums[i] * postfix[i + 1]
            else:
                postfix[i] = nums[i]

        for i in range(len(nums)):

            #edge case, first element
            #edge case, second element
            #normal case for the rest

            if i == 0:
                product[i] = postfix[i + 1]
            
            elif i == len(nums) - 1:
                product[i] = prefix[i - 1]

            else:
                product[i] = prefix[i - 1] * postfix[i + 1]

        return product
        