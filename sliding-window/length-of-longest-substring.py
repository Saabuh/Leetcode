# i overthought this question. Basically, you just have to notice that once you find a duplicate, you just shrink the window/
# subarray from the left until there is no more duplicates and you just do that by constantly removing from the set the
# value at l, which points to the value at the beginning of the subarray.
# this is because you dont have to check all of the intermediary subarrays which have duplicates, which is what i was fixated on.


class Solution:

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #
    #     # brute force solution
    #     longest = 0
    #     my_set = set()
    #
    #     for i in range(len(s)):
    #
    #         my_set.add(s[i])
    #
    #         for j in range(i + 1, len(s)):
    #             longest = max(longest, len(my_set))
    #
    #             if s[j] in my_set:
    #                 break
    #
    #             my_set.add(s[j])
    #
    #         my_set.clear()
    #
    #     return longest

    def lengthOfLongestSubstring(self, s: str) -> int:

        my_set = set()

        l = 0
        r = 0
        longest = 0

        for _ in range(len(s)):

            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1

            my_set.add(s[r])
            r += 1
            longest = max(longest, (r - l))

        return longest


solution = Solution()
print(solution.lengthOfLongestSubstring("abdabcbb"))
print(solution.lengthOfLongestSubstring("pwwkew"))
