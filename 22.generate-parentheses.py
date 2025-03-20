#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        sol = []

        if n == 1:
            return ["()"]

        def backtracking(open, close):
            if len(sol) == n * 2:
                ans.append("".join(sol))
                return

            if open < n:
                sol.append("(")
                backtracking(open + 1, close)
                sol.pop()
            if open > close:
                sol.append(")")
                backtracking(open, close + 1)
                sol.pop()

        backtracking(0, 0)
        return ans


# @lc code=end

# (()())
