#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
from typing import List


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        num = []
        start = 0
        n = len(nums)
        if n == 0:
            return num
        for _ in range(1, n + 1):
            if _ == n or nums[_] != nums[_] - 1:
                num.append(f"{nums[_]}")
            else:
                num.append(f"{nums[start]}->{nums[_ - 1]}")
            start += 1
        return num


# @lc code=end
