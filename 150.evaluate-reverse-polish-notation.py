#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
from math import ceil, floor


# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        let = []

        for token in tokens:
            if token in "+-*/":
                b, a = let.pop(), let.pop()
                if token == "+":
                    let.append(a + b)
                elif token == "-":
                    let.append(a - b)
                elif token == "*":
                    let.append(a * b)
                else:
                    c = a / b
                    if c < 0:
                        let.append(ceil(c))
                    else:
                        let.append(floor(c))
            else:
                let.append(int(token))

        return let[0]


# @lc code=end
