class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        matrix_len = len(matrix) - 1
        array_len = len(matrix[0]) - 1
        r = matrix_len
        middle_array = 0

        while l <= r:

            middle_array = ((r - l) // 2) + l

            if target >= matrix[middle_array][0] and target <= matrix[middle_array][array_len]:

                l = 0
                r = len(matrix[0]) - 1
                nums = matrix[middle_array]
                break

            elif target > matrix[middle_array][0]:

                l = middle_array + 1

            elif target < matrix[middle_array][array_len]:

                r = middle_array - 1

        while l <= r:
            middle = ((r - l) // 2) + l

            if nums[middle] == target:
                return True
            elif nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1

        return False





        