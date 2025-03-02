#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summ = 0
        n = len(nums)
        count_min = float("inf")

        for r in range(n):
            summ += nums[r]
            while summ >= target:
                count_min = min(count_min, r - l + 1)
                summ -= nums[l]
                l += 1

        return count_min if count_min < float("inf") else 0


# @lc code=end
