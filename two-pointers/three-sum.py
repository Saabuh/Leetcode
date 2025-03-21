# https://leetcode.com/problems/3sum/


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        # sort the array
        nums.sort()

        # initialize
        for i in range(len(nums) - 2):

            # ignore duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append((nums[i], nums[l], nums[r]))

                    # ignore duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

        return result


solution = Solution()

print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
