#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        while l < r:
            m = l + (r - l) // 2
            total = 0

            for pile in piles:
                total += math.ceil(pile / m)

            if total <= h:
                r = m
            else:
                l = m + 1

        return l


# @lc code=end
