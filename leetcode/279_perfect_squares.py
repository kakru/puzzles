#/usr/bin/env python3
import unittest

class Solution:  # DP is quite slow... 4080 ms (20.42%), 12.8 MB (100.00%)
    def numSquares(self, n: 'int') -> 'int':
        values = list(i**2 for i in range(1, int(n**0.5)+1))
        sq = list(i for i in range(n+1))
        sq[0] = 0
        for v in values: sq[v] = 1
        for i in range(5, n+1):  # for 1,2,3 => 1, for 4: 1, so starting from 5
            for v in values:
                if i < v: continue
                sq[i] = min(sq[i], sq[i-v] + 1)
        return sq[n]


# from collections import deque
# class Solution:  # BFS on stack, but Memory Limit Exceeded
#     def numSquares(self, n: 'int') -> 'int':
#         # (a, b, c), where:
#         # a = square value on this tree level, so: 1, 4, 9, etc.
#         # b = current tree leve
#         # c = counter of this level branching (so 1 for 1, 2 for 4, 3 for 9, etc.)
#         #     this is used to make sure that the checked sequence of numbers
#         #     is non-decreasing, so we'd check 4+9, but not 9+4
#         stack = deque([(i**2, 1, i) for i in range(1, int(n**0.5)+1)])
#         while True:
#             p, lvl, max_v_sqrt = stack.popleft()
#             if p == n: return lvl
#             for i in range(1, min(int(n**0.5), max_v_sqrt)+1):
#                 v = i*i
#                 if p+v <= n:
#                     stack.append((p+v, lvl+1, v))



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 12
        expected_output = 3
        output = Solution().numSquares(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 13
        expected_output = 2
        output = Solution().numSquares(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 7168
        expected_output = 4
        output = Solution().numSquares(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = 1
        expected_output = 1
        output = Solution().numSquares(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = 25
        expected_output = 1
        output = Solution().numSquares(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)