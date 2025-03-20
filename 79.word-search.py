#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)

        if m == 1 and n == 1:
            return board[0][0] == word

        def backttracking(pos, index):
            i, j = pos
            if index == w:
                return True

            if board[i][j] != word[index]:
                return False

            char = board[i][j]

            board[i][j] = "#"

            for i_plus, j_plus in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                c, b = i + i_plus, j + j_plus

                if 0 <= c < m and 0 <= b < n:
                    if backttracking((c, b), index + 1):
                        return True

            board[i][j] = char

            return False

        for i in range(m):
            for j in range(n):
                if backttracking((i, j), 0):
                    return True

        return False


# @lc code=end
