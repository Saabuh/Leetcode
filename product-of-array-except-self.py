from typing import List


class Solution:
    # O(n) time, O(n) space, no division
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #
    #     pre = [1] * len(nums)
    #     post = [1] * len(nums)
    #     res = []
    #
    #     # fill pre array: at each index, multiply value at prev index by the product of all previous indexes
    #     for i in range(1, len(nums)):
    #         pre[i] = nums[i - 1] * pre[i - 1]
    #
    #     # fill post array: at each index, multiply value at next index by the product of all next indexes
    #     for i in range(len(nums) - 2, -1, -1):
    #         post[i] = nums[i + 1] * post[i + 1]
    #
    #     for i in range(len(pre)):
    #         res.append(pre[i] * post[i])
    #
    #     return res

    # O(n) time, O(1) space excluding result array
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        main idea behind this question is that you want to always keep track of the product of a prefix and suffix
        at any particular index. One approach to this is having a prefix and suffix array, each holding the product of prefixes at any given index.

        then, at each index, you can multiply the previous value by the previous index to get the new prefix for that particular index.

        other option is holding a running prefix/suffix, shown below.
        """

        # pre/post will always represent the product of all prefixes/suffixes
        pre = 1
        post = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]

        for i in range(len(nums) - 1, -1, -1):

            res[i] *= post
            post *= nums[i]
            print(res, post)

        return res


solution = Solution()

solution.productExceptSelf([1, 2, 3, 4])
