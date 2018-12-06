#/usr/bin/env python3
import unittest


class Solution:  # 2364ms
    EMPTY = "."
    def isValidSudoku(self, board):
        seen = []
        for i, row in enumerate(board):
            for j, digit in enumerate(row):
                if digit != '.':
                    # seen.append((i, digit))  # numbers in rows are unique "by design"
                    seen.append((digit, j))
                    seen.append((i // 3, j // 3, digit))
        return len(seen) == len(set(seen))

    def firstEmpty(self, board):
        for j in range(9):
            if self.EMPTY in board[j]:
                return j, board[j].index(self.EMPTY)

    def solve(self, board, counter=0):
        numbers = set(str(i) for i in range(1,10))
        try:
            y, x = self.firstEmpty(board)
        except TypeError:
            return board
        for n in numbers - set(board[y]):
            board[y][x] = n
            if self.isValidSudoku(board):
                result = self.solve(board, counter+1)
                if self.firstEmpty(result) == None:
                    return result
            board[y][x] = self.EMPTY
        return board

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        board = self.solve(board)


class Solution:  # 2996ms
    EMPTY = "."
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def solve(board, fields):
            if not fields:
                return
            y, x = fields.pop()
            for k in "123456789":
                row = (board[y][i] for i in range(9))
                col = (board[i][x] for i in range(9))
                box = (board[i+y//3*3][j+x//3*3] for i in range(3) for j in range(3))
                if not any([ k in row, k in col, k in box ]):
                    board[y][x] = k
                    solve(board, fields)
                    if not fields:
                        return
            board[y][x] = self.EMPTY
            fields.append((y, x))

        fields = [(y,x) for y in range(9) for x in range(9)
                        if board[y][x] == self.EMPTY]
        solve(board, fields)


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
        output = [["5","3","4","6","7","8","9","1","2"],
                ["6","7","2","1","9","5","3","4","8"],
                ["1","9","8","3","4","2","5","6","7"],
                ["8","5","9","7","6","1","4","2","3"],
                ["4","2","6","8","5","3","7","9","1"],
                ["7","1","3","9","2","4","8","5","6"],
                ["9","6","1","5","3","7","2","8","4"],
                ["2","8","7","4","1","9","6","3","5"],
                ["3","4","5","2","8","6","1","7","9"]]
        Solution().solveSudoku(input_)  # in-place
        self.assertEqual(input_, output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    
