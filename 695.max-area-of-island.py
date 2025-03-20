#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#


# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_islands = 0

        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != 1:
                return 0
            else:
                grid[i][j] = 0
                return 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_islands = max(max_islands, dfs(i, j))

        return max_islands


# @lc code=end
