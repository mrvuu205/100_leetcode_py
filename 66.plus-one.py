#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        elif len(digits) == 1 and digits[-1] == 9:
            return [1, 0]
        else:
            digits[-1] = 0
            digits[len(digits) - 2] += 1

            return digits


# @lc code=end
