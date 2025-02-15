from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        my_set = set()
        longest = 0

        for num in nums:
            my_set.add(num)

        for num in my_set:

            count = 0
            inc = num

            # check if number can start a sequence
            if num - 1 not in my_set:

                # count the sequence
                while inc in my_set:
                    count += 1
                    inc += 1

            if count > longest:
                longest = count

        print(longest)


solution = Solution()

solution.longestConsecutive([1, 2, 5, 6, 100, 4, 2])
