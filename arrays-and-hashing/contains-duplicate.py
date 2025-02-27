class Solution(object):
    # def containsDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
    #
    #     return False

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # define set, lookup time in set is O(1)
        my_set = set()

        for num in nums:
            if num in my_set:
                return True

            my_set.add(num)

        return False


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([1, 2, 3, 4]))
