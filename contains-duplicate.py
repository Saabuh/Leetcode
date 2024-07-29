# https://leetcode.com/problems/contains-duplicate/
# 217

# pylint: disable=R


class Solution(object):
    def contains_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        my_dict = {}

        for num in nums:
            if num in my_dict:
                return True
            else:
                my_dict[num] = 1

        return False


solution = Solution()
print(solution.contains_duplicate([1, 2, 3, 1]))
print(solution.contains_duplicate([1, 2, 3, 4]))
print(solution.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
