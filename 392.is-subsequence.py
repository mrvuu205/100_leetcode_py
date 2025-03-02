#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        for _ in range(0, len(t)):
            if s[i] == t[_]:
                i += 1
            if i == len(s):
                break
        return i == len(s)


# @lc code=end
