from typing import List

#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num = [1] * n

        pre = 1
        for i in range(n - 1, -1, -1):
            num[i] = pre
            pre *= nums[i]

        suf = 1
        for i in range(n):
            num[i] *= suf
            suf *= nums[i]

        return num


# @lc code=end
