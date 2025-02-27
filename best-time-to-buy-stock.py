from typing import List

# the key to this question is that we start with 2 pointers pointing to day 1 and day 2. When we find a pair of days when
# the profit is greater than the previous max profit, we replace it and move the pointer pointing to the future day to the
# next day, since there is potentially a better day to sell off the stock. once we reach a day where there is no profit,
# that means we found a day where the buy price is even lower, so we use that day instead and see if there are future days
# that generate even more profit.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        maxProfit = 0

        if len(prices) == 1:
            return maxProfit

        for _ in range(len(prices) - 1):

            diff = prices[r] - prices[l]

            # print(f"left {prices[l]} right {prices[r]}")
            # print(diff)

            if diff > 0:
                maxProfit = max(diff, maxProfit)
                r += 1
            else:
                l = r
                r = l + 1

        return maxProfit


# prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
solution = Solution()
print(solution.maxProfit(prices))
