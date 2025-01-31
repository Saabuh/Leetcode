# https://leetcode.com/problems/group-anagrams/description/


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # create dictionary
        my_dict = {}
        # result array
        result = []

        for word in strs:

            # sorts an interable (string), returns a sorted list of iterable, join() joins the iterable into a single string
            sorted_str = "".join(sorted(word))

            # check if the sorted word exists as a key in the dictionary
            if sorted_str in my_dict:

                # append str to list
                my_dict[sorted_str].append(word)
            else:

                # make the key the sorted str and the value the str
                my_dict[sorted_str] = [word]

        for value in my_dict.values():
            result.append(value)

        return result


solution = Solution()
print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
