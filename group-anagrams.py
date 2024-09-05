# https://leetcode.com/problems/group-anagrams/
# 49

# pylint: disable=R


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # declarations
        word_dict = {}
        output = []

        # for every sorted word, check if it exists in the dictionary, if yes -> add original word as V to sorted word K, if no -> add sorted word as K, original word as V
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in word_dict:
                word_dict[sorted_word].append(word)
            else:
                word_list = []
                word_list.append(word)
                word_dict[sorted_word] = word_list

        # print out the values as a list
        for value_list in word_dict.values():
            output.append(value_list)

        return output


solution = Solution()
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# words = [""]
words = ["a"]

print(solution.groupAnagrams(words))
# output = [["bat"],["nat","tan"],["ate","eat","tea"]]
