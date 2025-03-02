#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        ans = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            s = h * w
            ans = max(ans, s)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans


# @lc code=end
