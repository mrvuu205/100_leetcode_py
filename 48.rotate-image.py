#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#


# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n // 2):
                matrix[i][n - j - 1], matrix[i][j] = matrix[i][j], matrix[i][n - j - 1]

        return matrix


# @lc code=end
