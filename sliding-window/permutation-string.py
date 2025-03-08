class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        # fixed sliding window
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        l, r = 0, len(s1) - 1

        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord("a")] += 1
            count_s2[ord(s2[i]) - ord("a")] += 1

        while r < len(s2):

            if count_s1 == count_s2:
                return True

            r += 1

            if r >= len(s2):
                return False

            count_s2[ord(s2[r]) - ord("a")] += 1
            count_s2[ord(s2[l]) - ord("a")] -= 1
            l += 1

        return False


solution = Solution()
s1 = "abcd"
s2 = "lecabee"
print(solution.checkInclusion(s1, s2))
