#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#


# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num

        while l <= r:
            m = (r + l) // 2
            squar = m * m

            if squar == num:
                return True
            elif squar < num:
                l = m + 1
            else:
                r = m - 1

        return False


# @lc code=end
