#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        r = m * n - 1

        while l <= r:
            mid = (l + r) // 2
            i = mid // m
            j = mid % m

            if target < matrix[i][j]:
                r = mid - 1
            elif target > matrix[i][j]:
                l = mid + 1
            else:
                return True

        return False


# @lc code=end
