#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        sol = []
        summ = 0
        n = len(candidates)

        def backtrack(x):
            nonlocal summ
            if summ == target:
                ans.append(sol[:])
                return
            if summ > target:
                return

            for i in range(x, n):
                sol.append(candidates[i])
                summ += candidates[i]
                backtrack(i)
                sol.pop()
                summ -= candidates[i]

        backtrack(0)
        return ans


# @lc code=end
