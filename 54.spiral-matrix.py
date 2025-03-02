#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from typing import List


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        n, m = len(matrix), len(matrix[0])

        UP_wall = 0
        DOWN_wall = n
        LEFT_wall = -1
        RIGHT_wall = m

        res = []
        i, j = 0, 0

        UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
        dic = RIGHT
        while len(res) != n * m:
            if dic == RIGHT:
                while j < RIGHT_wall:
                    res.append(matrix[i][j])
                    j += 1
                RIGHT_wall -= 1
                i, j = i + 1, j - 1
                dic = DOWN
            elif dic == DOWN:
                while i < DOWN_wall:
                    res.append(matrix[i][j])
                    i += 1
                DOWN_wall -= 1
                i, j = i - 1, j - 1
                dic = LEFT
            elif dic == LEFT:
                while j > LEFT_wall:
                    res.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                dic = UP
                LEFT_wall += 1
            else:
                while i > UP_wall:
                    res.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                dic = RIGHT
                UP_wall += 1

        return res


# @lc code=end
