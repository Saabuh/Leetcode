# https://leetcode.com/problems/container-with-most-water/description/


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maxArea = 0
        l, r = 0, len(height) - 1

        while l < r:
            bar1 = height[l]
            bar2 = height[r]

            if bar1 < bar2:
                newArea = bar1 * (r - l)
            else:
                newArea = bar2 * (r - l)

            maxArea = max(maxArea, newArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea


solution = Solution()
print(solution.maxArea([1, 2, 4, 3]))
