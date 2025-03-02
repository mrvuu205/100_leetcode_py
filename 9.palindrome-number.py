#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        for i, char in enumerate(str(x)):
            if char != str(x)[len(str(x)) - i - 1]:
                return False
        return True


# @lc code=end
