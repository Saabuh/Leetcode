from typing import List


class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #
    #     ## base case
    #     if not nums:
    #         return -1
    #
    #     if len(nums) == 1:
    #         if nums[0] != target:
    #             return -1
    #
    #     ##recursive step
    #     half_index = len(nums) // 2
    #     value = nums[half_index]
    #
    #     print(nums)
    #
    #     if target == value:
    #         return half_index
    #     elif target < value:
    #         return self.search(nums[:half_index], target)
    #     else:
    #         return half_index + self.search(nums[half_index:], target)

    def search(self, nums: List[int], target: int) -> int:
        """function docstring"""

        return self.helper(nums, target, 0, len(nums) - 1)

    def helper(self, nums: List[int], target: int, min_index: int, max_index: int):

        ## base case
        if min_index > max_index:
            return -1

        ## recursive step

        half_index = min_index + (max_index - min_index) // 2
        value = nums[half_index]
        print(value)

        if target == value:
            return half_index
        elif target < value:
            return self.helper(nums, target, min_index, half_index - 1)
        else:
            return self.helper(nums, target, half_index + 1, max_index)


solution = Solution()

print(solution.search([-1, 0, 3, 5, 9, 12], 2))
