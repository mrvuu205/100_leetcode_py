#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        sol = []

        if digits == "":
            return []
        letter_digit = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtracking(i=0):
            if i == len(digits):
                ans.append("".join(sol))
                return

            for letter in letter_digit[digits[i]]:
                sol.append(letter)
                backtracking(i + 1)
                sol.pop()

        backtracking(0)
        return ans


# @lc code=end
