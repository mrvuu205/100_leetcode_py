#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):

            if (
                i < 0
                or i >= len(grid)
                or j < 0
                or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return
            else:
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        is_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    is_islands += 1
                    dfs(i, j)

        return is_islands


# @lc code=end
