#/usr/bin/env python3
import unittest

# class Solution:  # 52ms, best LeetCode solution
#     def isValidSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#         seen = []
#         for i, row in enumerate(board):
#             for j, digit in enumerate(row):
#                 if digit != '.':
#                     seen.append((i, digit))
#                     seen.append((digit, j))
#                     seen.append((i // 3, j // 3, digit))
#         return len(seen) == len(set(seen))

class Solution:  # 60 ms
    EMPTY = "."
    def validInRows(self, board):
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != self.EMPTY and board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
        return True
    
    def validInCols(self, board):
        return self.validInRows(list(zip(*board)))
    
    def validInBoxes(self, board):
        for by in (0, 3, 6):
            for bx in (0, 3, 6):
                grp = [board[by][bx], board[by][bx+1], board[by][bx+2],
                       board[by+1][bx], board[by+1][bx+1], board[by+1][bx+2],
                       board[by+2][bx], board[by+2][bx+1], board[by+2][bx+2]]
                grp = [g for g in grp if g != self.EMPTY]
                if len(set(grp)) != len(grp):
                    return False
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return (self.validInRows(board) and
                self.validInCols(board) and
                self.validInBoxes(board))



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
        expected_output = True
        output = Solution().isValidSudoku(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [["8","3",".",".","7",".",".",".","."],
                  ["6",".",".","1","9","5",".",".","."],
                  [".","9","8",".",".",".",".","6","."],
                  ["8",".",".",".","6",".",".",".","3"],
                  ["4",".",".","8",".","3",".",".","1"],
                  ["7",".",".",".","2",".",".",".","6"],
                  [".","6",".",".",".",".","2","8","."],
                  [".",".",".","4","1","9",".",".","5"],
                  [".",".",".",".","8",".",".","7","9"]]
        expected_output = False
        output = Solution().isValidSudoku(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
