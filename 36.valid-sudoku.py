#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # duyet qua tung hang neu tat ca deu dung tra ve 1
        # duyet qua tung cot neu tat ca deu dung tra ve 1
        # duyet qua tung o 3x3 neu k trung nhau tra ve 1
        # neu ca 3 = 1 thi tra ve true
        # duyet qua tung hang
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]

                if item in s:
                    return False
                elif item != ".":

                    s.add(item)

        # duyet qua tung cot
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]

                if item in s:
                    return False
                elif item != ".":
                    s.add(item)

        # duyet qua tung o
        start = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

        for i, j in start:
            s = set()
            for row in range(i, i + 3):
                for cow in range(j, j + 3):
                    item = board[row][cow]

                    if item in s:
                        return False
                    elif item != ".":
                        s.add(item)

        return True


# @lc code=end
