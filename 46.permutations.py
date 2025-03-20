#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        sol = []

        def backtrack(i):

            if i == len(nums):
                ans.append(sol[:])
                return

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack(i + 1)
                    sol.pop()

        backtrack(0)
        return ans


# @lc code=end
