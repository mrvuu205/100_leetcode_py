#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n

        while l < r:
            m = (r + l) // 2

            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l


# 0 1 2 3 4 5

# @lc code=end
