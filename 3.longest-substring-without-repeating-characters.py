#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_sub = 0
        l = 0
        n = len(s)
        sett = set()

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            w = (r - l) + 1

            long_sub = max(long_sub, w)

        return long_sub


# @lc code=end
