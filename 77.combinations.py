#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, sol = [], []

        def backtracking(i):
            if len(sol) == k:
                ans.append(sol[:])
                return
            left = i
            still_need = k - len(sol)

            if left > still_need:
                backtracking(i - 1)

            sol.append(i)
            backtracking(i - 1)
            sol.pop()

        backtracking(n)
        return ans


# @lc code=end
