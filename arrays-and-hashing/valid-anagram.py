class Solution(object):

    # version 1
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        my_dict1 = {}
        my_dict2 = {}

        for char in s:
            if char in my_dict1:
                my_dict1[char] += 1
            else:
                my_dict1[char] = 1

        for char in t:
            if char in my_dict2:
                my_dict2[char] += 1
            else:
                my_dict2[char] = 1

        return my_dict1 == my_dict2

    # version 2
    def isAnagram2(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

    # version 3 (solves for unicode character inputs)
    def isAnagram3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1

        for val in count:
            if val != 0:
                return False
        return True


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "cat"))
