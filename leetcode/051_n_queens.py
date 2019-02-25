#/usr/bin/env python3
import unittest

# class Solution:  # 1968 ms (5.04%)
#     def solveNQueens(self, n: 'int') -> 'List[List[str]]':
#         def presentBoard(c):  # no horizontal/vertical collisions by design
#             return ["." * c[i] + "Q" + "." * (n-c[i]-1) for i in range(n)]
#         def checkBoard(b):  # checking only diagonal collisions
#             for row in range(n):
#                 if any(abs(b[i] - b[row]) == i-row for i in range(row+1, n)):
#                     return False
#             return True        
#         results = []
#         def helper(board):
#             if len(board) == n:
#                 if checkBoard(board):
#                     results.append(presentBoard(board))
#             else:
#                 for i in list(set(range(n)) - set(board)):
#                     board.append(i)
#                     helper(board)
#                     board.pop()
#         helper([])  # backtracking
#         return results


# class Solution:  # 1516 ms (5.04%)
#     def solveNQueens(self, n: 'int') -> 'List[List[str]]':
#         def presentBoard(c):  # no horizontal/vertical collisions by design
#             return ["." * c[i] + "Q" + "." * (n-c[i]-1) for i in range(n)]
#         def checkBoard(b):  # checking only diagonal collisions
#             for row in range(n):
#                 if any(abs(b[i] - b[row]) == i-row for i in range(row+1, n)):
#                     return False
#             return True        
#         results = []
#         def helper(board, options):
#             if not options:
#                 if checkBoard(board):
#                     results.append(presentBoard(board))
#             else:
#                 for i, o in enumerate(options):
#                     board.append(o)
#                     helper(board, options[:i] + options[i+1:])
#                     board.pop()
#         helper([], list(range(n)))  # backtracking
#         return results


from itertools import permutations
class Solution:  # 896 ms (5.04%)
    def solveNQueens(self, n: 'int') -> 'List[List[str]]':
        def presentBoard(c):  # no horizontal/vertical collisions by design
            return ["." * c[i] + "Q" + "." * (n-c[i]-1) for i in range(n)]
        def checkBoard(b):  # checking only diagonal collisions
            for row in range(n):
                if any(abs(b[i] - b[row]) == i-row for i in range(row+1, n)):
                    return False
            return True        
        results = []
        for c in permutations(range(n), n):
            if checkBoard(c): results.append(presentBoard(c))
        return results


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 4
        print()
        expected_output = [[".Q..",  # Solution 1 of 2
                            "...Q",
                            "Q...",
                            "..Q."],
                           ["..Q.",  # Solution 2 of 2
                            "Q...",
                            "...Q",
                            ".Q.."]]
        output = Solution().solveNQueens(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
