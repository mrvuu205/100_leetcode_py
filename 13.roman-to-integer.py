#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i, char in enumerate(s):
            if i < len(s) - 1 and roman_to_int[char] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[char]
            else:
                result += roman_to_int[char]
        return result


# @lc code=end
