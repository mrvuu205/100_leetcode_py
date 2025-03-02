#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        strs.sort()

        fist = strs[0]
        last = strs[-1]

        key = []

        for i in range(len(fist)):
            if i < len(last) and fist[i] == last[i]:
                key.append(fist[i])
            else:
                break

        return "".join(key)


# @lc code=end
