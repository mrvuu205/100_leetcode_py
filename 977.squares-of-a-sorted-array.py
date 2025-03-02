#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#


# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1

            else:
                result.append(nums[right] ** 2)
                right -= 1
        result = result[::-1]
        return result


# @lc code=end
