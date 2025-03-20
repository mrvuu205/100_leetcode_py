#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sol = []

        def backchacking(i):
            if i == len(nums):
                ans.append(sol[:])
                return

            backchacking(i + 1)

            sol.append(nums[i])
            backchacking(i + 1)
            sol.pop()

        backchacking(0)
        return ans


# @lc code=end
