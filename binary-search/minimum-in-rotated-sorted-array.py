from typing import List

# the idea here is that when performing a binary search, all we have to do is check if the middle number is less than or
# greater than the number at index l. If the middle number is less than num[l], that means at some point in between, we hit the maximum and went back to the minimum. Else, it means that all the numbers between it are increasing. We are utilizing the
# fact that the array is sorted and that when we go from a larger number to a smaller number, that means we hit the maximum
# and minimum.


class Solution:
    # def findMin(self, nums: List[int]) -> int:
    #
    #     l = 0
    #     r = len(nums) - 1
    #     res = 9999
    #
    #     while l <= r:
    #
    #         mid = l + (r - l) // 2
    #         print(nums[mid])
    #
    #         if (r - l) == 1:
    #             return min(res, nums[l], nums[r])
    #
    #         if (r - l) == 0:
    #             return min(res, nums[l])
    #
    #         if nums[mid] < res:
    #             res = nums[mid]
    #         print(f"result: {res}")
    #
    #         if nums[mid] > nums[l] and nums[mid] > nums[r]:
    #             if nums[r] < nums[l]:
    #                 l = mid + 1
    #                 print(f"left {l} right {r}")
    #             else:
    #                 r = mid - 1
    #         elif nums[mid] < nums[l] and nums[mid] < nums[r]:
    #             if nums[l] > nums[r]:
    #                 print("here")
    #                 r = mid - 1
    #             else:
    #                 l = mid + 1
    #         else:
    #             return min(res, nums[l])
    #
    #     return res
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res


nums = [6, 7, 8, 1, 2, 3, 4, 5]
# nums = [4, 5, 6, 7, 0, 1, 2]
# nums = [2, 1]
solution = Solution()
print(solution.findMin(nums))
