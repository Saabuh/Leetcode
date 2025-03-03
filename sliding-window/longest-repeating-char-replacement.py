class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, r = 0, 0
        count = 0
        last = ""
        longest = 0

        for l in range(len(s)):

            if s[l] == last:
                continue

            last = s[l]
            r = l

            while count <= k and r <= len(s):
                print(f"left {l} right {r}")
                longest = max(longest, r - l)

                if r >= len(s):
                    break

                if s[r] != s[l]:
                    count += 1

                print(f"count {count}")
                r += 1

            count = 0
            print(longest)

        return longest


s = "AABABBA"
# s = "ABAB"
solution = Solution()
print(solution.characterReplacement(s, 2))
