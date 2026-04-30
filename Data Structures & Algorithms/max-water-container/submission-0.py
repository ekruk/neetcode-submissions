class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1

        temp_max = 0
        final_max = 0

        while l < r:

            temp_max = min(heights[l], heights[r]) * (r - l)
            final_max = max(final_max, temp_max)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1

            else:
                l += 1
                r -= 1

        return final_max


        