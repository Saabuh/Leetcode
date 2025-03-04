# the key idea behind this question is that we want to know 1. whats the majority char in our subarray and 2. if the total # of minority char
# in our subarray is <= k at all times. if it is, that means that we can change all the characters to a single character to form a potential longest
# char string. if it exceeds that, we wouldnt know what characters to change in the subarray to create the longest subarray, so we either shrink the
# subarray or we ignore it.


class Solution:
    # def characterReplacement(self, s: str, k: int) -> int:
    #
    #     l, r = 0, 0
    #     count = 0
    #     last = ""
    #     longest = 0
    #
    #     for l in range(len(s)):
    #
    #         if s[l] == last:
    #             continue
    #
    #         last = s[l]
    #         r = l
    #
    #         while count <= k and r <= len(s):
    #             # print(f"left {l} right {r}")
    #             longest = max(longest, r - l)
    #
    #             if r >= len(s):
    #                 break
    #
    #             if s[r] != s[l]:
    #                 count += 1
    #
    #             # print(f"count {count}")
    #             r += 1
    #
    #         count = 0
    #         # print(longest)
    #
    #     return longest

    # def characterReplacement(self, s: str, k: int) -> int:
    #     """slow, O(n^2) solution"""
    #
    #     longest = 0
    #
    #     for i in range(len(s)):
    #         freq = {}
    #         maj = 0
    #         for j in range(i, len(s)):
    #             freq[s[j]] = 1 + freq.get(s[j], 0)
    #             maj = max(maj, freq[s[j]])
    #
    #             if (j - i + 1) - maj <= k:
    #                 longest = max(longest, j - i + 1)
    #
    #     return longest
    #

    def characterReplacement(self, s: str, k: int) -> int:
        """O(n) solution"""

        l = 0
        longest = 0
        maj = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            maj = max(freq.values())

            if (r - l + 1) - maj <= k:
                longest = max(longest, r - l + 1)
            else:
                # not recalculating the majority makes this condition assume that its always shifting from a minority character, which is fine because
                # we still decrement the frequency and recalculate it after the while loop. If it's still invalid, it'll go through this again, which
                # is better than recalculating the max at every step.
                while (r - l + 1) - maj > k:
                    freq[s[l]] = freq.get(s[l], 0) - 1
                    l += 1

        return longest


s = "AABABBA"
# s = "ABAB"
solution = Solution()
print(solution.characterReplacement(s, 2))
