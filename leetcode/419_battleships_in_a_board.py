#/usr/bin/env python3
import unittest

class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        width = len(board[0])
        counter = 0
        for y in range(len(board)):
            for x in range(width):
                # there are the following options:
                if board[y][x] == SHP:
                    if x > 0 and board[y][x-1] == 'X':
                        # 1. it's the continuation of the ship horizontaly (another X on the left)
                        continue
                    elif y > 0 and board[y-1][x] == 'X':
                        # 2. it's the continuation of the ship verticaly (another X on the top)
                        continue
                    else:
                        # 3. it's the first X of the ship
                        counter += 1
                # 4. or it's not a ship (.)
        return counter


class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        width = len(board[0])
        counter = 0
        for y in range(len(board)):
            for x in range(width):
                if ((board[y][x] == 'X') and
                    ((x == 0 or board[y][x-1] != 'X') and
                     (y == 0 or board[y-1][x] != 'X'))):
                        counter += 1
        return counter



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = """X..X
                    ...X
                    ...X""".replace(' ', '').split('\n')
        expected_output = 2
        output = Solution().countBattleships(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
