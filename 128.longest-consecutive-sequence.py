#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        num = set(nums)

        for s in num:
            if s - 1 not in num:
                next_s = s + 1
                length = 1
                while next_s in num:
                    length += 1
                    next_s += 1
                count = max(count, length)

        return count


# @lc code=end
