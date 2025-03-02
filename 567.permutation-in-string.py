#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        count_n1 = [0] * 26
        count_n2 = [0] * 26

        if n1 > n2:
            return False

        for i in range(n1):
            count_n1[ord(s1[i]) - 97] += 1
            count_n2[ord(s2[i]) - 97] += 1

        if count_n1 == count_n2:
            return True

        for i in range(n1, n2):
            count_n2[ord(s2[i]) - 97] += 1
            count_n2[ord(s2[i - n1]) - 97] -= 1

            if count_n1 == count_n2:
                return True

        return False


# @lc code=end
