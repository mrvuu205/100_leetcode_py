#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        h = set()
        n = len(nums)

        for num in nums:
            if num in h:
                return True
            else:
                h.add(num)

        return False


# @lc code=end
