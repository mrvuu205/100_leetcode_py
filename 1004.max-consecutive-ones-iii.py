#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#


# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_one = 0
        num_zero = 0
        n = len(nums)

        for r in range(n):

            if nums[r] == 0:
                num_zero += 1

            while num_zero > k:
                if nums[l] == 0:
                    num_zero -= 1
                l += 1

            w = r - l + 1
            max_one = max(w, max_one)
        return max_one


# @lc code=end
