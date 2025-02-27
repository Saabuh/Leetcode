from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = set()
        col = [set() for _ in range(9)]

        for c in board:

            # check for unique values in a given row and column
            for i, r in enumerate(c):
                print("row: ", r)
                if r in row and r != ".":
                    return False

                if r in col[i] and r != ".":
                    return False
                col[i].add(r)
                row.add(r)

            row.clear()

        return True


input = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

solution = Solution()
print(solution.isValidSudoku(input))
