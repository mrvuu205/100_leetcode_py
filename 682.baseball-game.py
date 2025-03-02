#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#


# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for _ in operations:

            if _ == "C":
                ans.pop()
            elif _ == "D":
                ans.append(ans[-1] * 2)
            elif _ == "+":
                ans.append(ans[-1] + ans[-2])
            else:
                ans.append(int(_))

        return sum(ans)


# @lc code=end
