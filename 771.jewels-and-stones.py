#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#


# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in jewels:
            for j in stones:
                if i == j:
                    count += 1

        return count


# @lc code=end
