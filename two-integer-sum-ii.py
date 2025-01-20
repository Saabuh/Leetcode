from typing import List


class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #
    #     for i in range(1, len(numbers) + 1):
    #         for j in range(i + 1, len(numbers) + 1):
    #
    #             if numbers[i - 1] + numbers[j - 1] == target:
    #                 return [i, j]
    #
    #     return []

    # def twoSum(self, numbers, target):
    #
    #     # use the two-pointer algorithm
    #     for i in range(len(numbers), 1, -1):
    #
    #         for j in range(1, len(numbers) + 1):
    #
    #             if numbers[i - 1] + numbers[j - 1] > target:
    #                 break
    #
    #             if numbers[i - 1] + numbers[j - 1] == target:
    #                 return [j, i]
    #
    #     return []

    # two-pointer
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1


solution = Solution()
print(solution.twoSum([1, 2, 3, 4], 3))
