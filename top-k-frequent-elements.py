from typing import List


class Solution(object):
    ## O(nlogn) solution
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #
    #     # use dict, (hashmap implementation)
    #     my_dict = {}
    #     result = []
    #
    #     for num in nums:
    #         if num in my_dict:
    #             my_dict[num] += 1
    #         else:
    #             my_dict[num] = 1
    #
    #     # sort dictionary (nlogn) time
    #     sorted_dict = dict(
    #         sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
    #     )
    #
    #     for i, key in enumerate(sorted_dict.keys()):
    #         if i < k:
    #             result.append(key)
    #
    #     return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # array holding the frequency of each number
        count = [0] * 10

        for num in nums:
            # count[ord(str(num)) - ord("0")] += 1
            count[num] += 1


solution = Solution()
print(solution.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
