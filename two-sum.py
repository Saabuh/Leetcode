class Solution(object):

    # brute force O(n^2)
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #
    #     for i in range(len(nums) - 1):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    #
    #     return [0, 0]

    # faster solution  O(n)
    def twoSum(self, nums, target):
        #     """
        #     :type nums: List[int]
        #     :type target: int
        #     :rtype: List[int]
        #     """

        # use a hashmap, O(1) lookup time
        my_map = {}

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in my_map:
                return [i, my_map.get(diff)]

            my_map[nums[i]] = i

        return [0, 0]


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
