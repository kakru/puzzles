#/usr/bin/env python3
import unittest

class Solution:  # 32 ms (100.00%), 12.4 MB (100.00%)
    def uniquePaths(self, m: 'int', n: 'int') -> 'int':
        if m < 1 or n < 1: return 0
        a = [[1 for _ in range(m)] for _ in range(n)]
        for j in range(1, n):
            for i in range(1, m):
                a[j][i] = a[j-1][i] + a[j][i-1]
        return a[-1][-1]


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 3, 2
        expected_output = 3
        output = Solution().uniquePaths(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 7, 3
        expected_output = 28
        output = Solution().uniquePaths(*input_)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main(verbosity=2)
