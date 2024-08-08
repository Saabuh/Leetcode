# https://leetcode.com/problems/two-sum/
# 1

# pylint: disable=R


class Solution(object):
    # hashmap solution
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        my_dict = {}
        results = []

        for i, num in enumerate(nums):

            dif = target - num

            if dif in my_dict:
                results.append(my_dict[dif])
                results.append(i)
                return results
            else:
                my_dict[num] = i

    # brute force solution
    def twoSumBF(self, nums, target):

        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()
# print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSumBF([2, 7, 11, 15], 9))
