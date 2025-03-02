#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        count = 0

        for num in nums:
            if count == 0:
                ans = num

            count += 1 if ans == num else -1

        return ans


# @lc code=end
