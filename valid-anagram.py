# https://leetcode.com/problems/valid-anagram/
# 242

# pylint: disable=R


# first naive solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        my_dict = {}

        # add all characters from s to dictionary
        for letter in s:
            if letter in my_dict:
                my_dict[letter] = my_dict[letter] + 1
            else:
                my_dict[letter] = 1

        # remove characters from dictionary based on t
        for letter in t:
            if letter in my_dict:
                my_dict[letter] = my_dict[letter] - 1
            else:
                return False

        for key in my_dict:
            if my_dict[key] != 0:
                return False

        return True


solution = Solution()

print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
