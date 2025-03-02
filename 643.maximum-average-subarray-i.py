#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#


# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float("-inf")
        L_window = sum(nums[:k])
        max_avg = max(max_avg, L_window / k)

        for i in range(k, len(nums)):
            L_window += nums[i] - nums[i - k]
            max_avg = max(max_avg, L_window / k)

        return max_avg


# @lc code=end
