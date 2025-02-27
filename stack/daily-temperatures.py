from typing import List

# the idea behind this questions is that we want to always keep track of the daily temperatures that have not yet found a
# day where the daily temperature exceeded their own, so we have to keep track of its index. this works because our stack
# will always only have daily temperatures that havent found an exceeding daily temperature yet, so the stack is in
# monotonic decreasing order.


class Solution:
    # incomplete
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #
    #     prev = 30
    #     cur = 0
    #     c = 0
    #     highest = 0
    #     my_stack = []
    #     result = []
    #
    #     for temp in temperatures:
    #         my_stack.append(temp)
    #
    #     while my_stack:
    #
    #         cur = my_stack.pop()
    #
    #         if cur > highest:
    #             result.append(0)
    #             highest = cur
    #             prev = cur
    #             continue
    #
    #         if cur < prev:
    #             result.append(1)
    #             c = 1
    #         else:
    #             c += 1
    #             result.append(c)
    #
    #         prev = cur
    #
    #     result.reverse()
    #     return result

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        temps = []

        for i, temp in enumerate(temperatures):

            # if temp array is empty or if temperature does not exceed previous temperature
            if not temps or temp <= temps[-1][0]:
                temps.append([temp, i])
            else:
                while temps and temp > temps[-1][0]:
                    prev_temp = temps.pop()
                    result[prev_temp[1]] = i - prev_temp[1]

                temps.append([temp, i])

        return result


solution = Solution()

print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
