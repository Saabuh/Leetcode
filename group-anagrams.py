# https://leetcode.com/problems/group-anagrams/description/


class Solution(object):

    # def groupAnagrams(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     hashmap solution using sort
    #     """
    #
    #     # time complexity: O(m * nlogn)
    #     # space complexity: O(m * n)
    #
    #     # create dictionary
    #     my_dict = {}
    #     # result array
    #
    #     for word in strs:
    #
    #         # sorts an interable (string), returns a sorted list of iterable, join() joins the iterable into a single string
    #         sorted_str = "".join(sorted(word))
    #
    #         # check if the sorted word exists as a key in the dictionary
    #         if sorted_str in my_dict:
    #
    #             # append str to list
    #             my_dict[sorted_str].append(word)
    #         else:
    #
    #             # make the key the sorted str and the value the str
    #             my_dict[sorted_str] = [word]
    #
    #     return list(my_dict.values())

    def groupAnagrams(self, strs):
        """
        hashmap solution using just a hashmap
        """

        # dictionary
        my_dict = {}

        for s in strs:

            # character counting array
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            if tuple(count) in my_dict:
                my_dict[tuple(count)].append(s)
            else:
                my_dict[tuple(count)] = [s]

        return list(my_dict.values())


solution = Solution()
print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
