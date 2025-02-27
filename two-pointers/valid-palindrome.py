# https://leetcode.com/problems/valid-palindrome

import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # create list
        stack = []

        # clean string
        new_string = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        a = len(new_string) - 1
        b = 0

        while a != b and b < a and len(new_string) > 0:

            if new_string[a] != new_string[b]:
                return False

            a -= 1
            b += 1

        return True

    def isPalindrome2(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True


# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#
#         # create list
#         stack = []
#
#         # clean string
#         new_string = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
#
#         a = len(new_string) - 1
#         b = 0
#
#         while a != b and b < a and len(new_string) > 0:
#
#             if new_string[a] != new_string[b]:
#                 return False
#
#             a -= 1
#             b += 1
#
#         return True

# solution = Solution()
# solution.isPalindrome("A man, a plan, a canal: Panama")
# solution.isPalindrome("race a car")
# solution.isPalindrome(" ")
