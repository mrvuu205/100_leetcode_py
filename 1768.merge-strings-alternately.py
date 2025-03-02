#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#


# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        for _ in range(0, max(len(word1), len(word2))):
            if 2 * len(word1) > len(word3):
                word3 += word1[_]
            if 2 * len(word2) > len(word3):
                word3 += word2[_]
        return word3

    # merged = ''.join(a + b for a, b in zip(word1, word2))
    #     # Nối phần còn lại của chuỗi dài hơn (nếu có)
    #     return merged + word1[len(word2):] + word2[len(word1):]


# @lc code=end
