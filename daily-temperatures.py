from typing import List


class Solution:
    # incomplete
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        prev = 30
        cur = 0
        c = 0
        highest = 0
        my_stack = []
        result = []

        for temp in temperatures:
            my_stack.append(temp)

        while my_stack:

            cur = my_stack.pop()

            if cur > highest:
                result.append(0)
                highest = cur
                prev = cur
                continue

            if cur < prev:
                result.append(1)
                c = 1
            else:
                c += 1
                result.append(c)

            prev = cur

        result.reverse()
        return result


solution = Solution()

print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
