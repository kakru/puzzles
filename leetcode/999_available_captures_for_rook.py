#/usr/bin/env python3
import unittest

"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty
squares, white bishops, and black pawns.  These are given as characters
'R', '.', 'B', and 'p' respectively. Uppercase characters represent white
pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal
directions (north, east, west, and south), then moves in that direction
until it chooses to stop, reaches the edge of the board, or captures an
opposite colored pawn by moving to the same square it occupies.  Also,
rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
"""

# R = white rook
# . = empty square
# B = white bishop
# p = black pawn

class Solution:  # 52 ms (100%)
    def numRookCaptures(self, board: 'List[List[str]]') -> int:
        answer = 0
        # finding the rook position (R)
        for R_y in range(8):
            if 'R' in board[R_y]:
                R_x = board[R_y].index('R')
                break
        # R position in (R_y, R_x)
        # checking the row for pawns, -->
        for x in range(R_x + 1, 8):
            if board[R_y][x] == 'p':
                answer += 1  # a pawn can be captured
                break
            elif board[R_y][x] == 'B':
                break  # no pawn can be captured after
        # checking the row for pawns, <--
        for x in range(R_x - 1, -1, -1):
            if board[R_y][x] == 'p':
                answer += 1  # a pawn can be captured
                break
            elif board[R_y][x] == 'B':
                break  # no pawn can be captured after
        # checking the column for pawns, GOING DOWN
        for y in range(R_y + 1, 8):
            if board[y][R_x] == 'p':
                answer += 1  # a pawn can be captured
                break
            elif board[y][R_y] == 'B':
                break  # no pawn can be captured after
        # checking the column for pawns, GOING UP
        for y in range(R_y - 1, -1, -1):
            if board[y][R_x] == 'p':
                answer += 1  # a pawn can be captured
                break
            elif board[y][R_y] == 'B':
                break  # no pawn can be captured after
        return answer



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[".",".",".",".",".",".",".","."],
                  [".",".",".","p",".",".",".","."],
                  [".",".",".","R",".",".",".","p"],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".","p",".",".",".","."],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".","."]]
        expected_output = 3  # In this example the rook is able to capture all the pawns.
        output = Solution().numRookCaptures(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
        expected_output = 0  # Bishops are blocking the rook to capture any pawn.
        output = Solution().numRookCaptures(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
        expected_output = 3  # The rook can capture the pawns at positions b5, d6 and f5.
        output = Solution().numRookCaptures(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)