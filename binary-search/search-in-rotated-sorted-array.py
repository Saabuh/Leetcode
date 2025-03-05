from typing import List

# the key idea behind this problem is to recognize the properties of a sorted rotated array and how the middle
# number compares to the leftmost number. if you look at those numbers, if the middle number > leftmost number,
# that means all the numbers between it are constantly increasing. so if target is l <= target < mid, then
# its within that subarray. if middle number < leftmost number, that means between those numbers, it increases
# starting from leftmost number, hits a maximum, and goes back to the minimum, increasing towards the mid number.
# so if the target is < mid or target is > leftmost number, then its in that subarray. Else its in the other
# subarray.


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target < nums[mid] or target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


# nums = [3, 4, 5, 6, 1, 2]
# target = 1
nums = [3, 5, 6, 0, 1, 2]
target = 4
solution = Solution()
print(solution.search(nums, target))
