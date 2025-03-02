#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#
from collections import Counter


# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloons = "balloon"

        for t in text:
            if t in balloons:
                counter[t] += 1

        if any(t not in counter for t in balloons):
            return 0
        else:
            return min(
                counter["b"],
                counter["a"],
                counter["l"] // 2,
                counter["o"] // 2,
                counter["n"],
            )


# @lc code=end
