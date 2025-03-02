#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#


# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        max_rep = 0

        for right in range(len(s)):
            count[ord(s[right]) - ord("A")] += 1

            while (right - left + 1) - max(count) > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            max_rep = max(max_rep, right - left + 1)

        return max_rep


# @lc code=end
