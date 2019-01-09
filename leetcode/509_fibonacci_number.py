#/usr/bin/env python3
import unittest

# class Solution:
#     def fib(self, N):
#         """
#         :type N: int
#         :rtype: int
#         """
#         fibs = [0, 1]
#         for i in range(2, 31):
#             fibs.append(fibs[i-1] + fibs[i-2])
#         return fibs[N]

class Solution:
    def fib(self, N):
        # as 0 <= N <= 30, the best is to use the precalculated values:
        return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
                610, 987, 1597, 2584, 4181, 6765,10946, 17711, 28657,
                46368, 75025, 121393, 196418, 317811, 514229, 832040][N]


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 4
        expected_output = 3
        output = Solution().fib(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
