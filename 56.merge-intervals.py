#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#


# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda intervals: intervals[0])
        result = []

        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1] = [result[-1][0], max(result[-1][1], interval[1])]
        return result


# @lc code=end
