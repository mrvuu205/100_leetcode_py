#
# @lc app=leetcode id=2239 lang=python3
#
# [2239] Find Closest Number to Zero
#
from typing import List


# @lc code=start
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for num in nums:
            if abs(num) < abs(closest) or abs(closest) == abs(num) and closest < num:
                closest = num
        return closest


# @lc code=end
