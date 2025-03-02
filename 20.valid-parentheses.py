#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        key = []

        for i in s:
            if i in ["(", "{", "["]:
                key.append(i)
            elif i in [")", "}", "]"]:
                if not key:
                    return False
                if key[-1] == "(" and i == ")":
                    key.pop()
                elif key[-1] == "{" and i == "}":
                    key.pop()
                elif key[-1] == "[" and i == "]":
                    key.pop()
                else:
                    return False

        return not key


# @lc code=end
