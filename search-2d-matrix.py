from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchColumns(matrix, target, 0, len(matrix) - 1)

    def searchColumns(
        self, matrix: List[List[int]], target: int, min: int, max: int
    ) -> bool:

        # if min > max:
        #     return False
        # or
        if target < matrix[0][0]:
            return False

        half_index = min + (max - min) // 2
        value = matrix[half_index][0]

        ##checks edge case if target is in last row
        if (max - min) == 0:
            return self.searchRows(matrix, target, 0, len(matrix[0]) - 1, half_index)

        if target >= value and target < matrix[half_index + 1][0]:
            return self.searchRows(matrix, target, 0, len(matrix[0]) - 1, half_index)
        elif target < value:
            return self.searchColumns(matrix, target, min, half_index - 1)
        else:
            return self.searchColumns(matrix, target, half_index + 1, max)

    def searchRows(
        self, matrix: List[List[int]], target: int, min: int, max: int, column: int
    ) -> bool:

        ## base case:
        if min > max:
            return False

        half_index = min + (max - min) // 2
        value = matrix[column][half_index]

        if target == value:
            return True
        elif target < value:
            return self.searchRows(matrix, target, min, half_index - 1, column)
        else:
            return self.searchRows(matrix, target, half_index + 1, max, column)


solution = Solution()
# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
matrix = [[1], [3]]
print(solution.searchMatrix(matrix, 0))
# print(solution.searchMatrix(matrix, 30))
# print(solution.searchMatrix(matrix, 63))
