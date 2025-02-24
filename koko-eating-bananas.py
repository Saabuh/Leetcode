from typing import List
import math

## the key here is to notice that we can start with the pile with the most bananas P and see if we can eat P bananas/hr k
## to see if we finish all the bananas before time h is up. if we finish all the bananas in a given time H and H < h,
## then we can possibly eat slower but we still keep track of the possible answer k. else, we must increase out bananas/hr


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        return self.helper(piles, h, 1, max(piles), 0)

    def helper(self, piles: List[int], h: int, min: int, max: int, res: int) -> int:

        # base case
        if min > max:
            return res

        k = (min + max) // 2

        new_h = 0

        for pile in piles:
            new_h += math.ceil(pile / k)

        # print(f"min: {min}, max: {max}")
        # print(f"banans per hour: {k}, {new_h}")

        # if we're eating too fast, maybe we can eat slower
        if new_h <= h:
            return self.helper(piles, h, min, k - 1, k)
        else:
            return self.helper(piles, h, k + 1, max, res)


solution = Solution()
piles = [30, 11, 23, 4, 20]
h = 6

print(solution.minEatingSpeed(piles, h))
