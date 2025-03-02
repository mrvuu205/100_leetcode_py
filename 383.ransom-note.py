#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# form collections import Counter
from collections import Counter


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count_Note = Counter(ransomNote)
        count_Zine = Counter(magazine)

        for char, i in count_Note.items():
            if count_Zine[char] < i:
                return False

        return True


# @lc code=end
