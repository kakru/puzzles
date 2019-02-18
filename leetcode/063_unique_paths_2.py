#/usr/bin/env python3
import unittest

class Solution:  # 40 ms (59.05%), 12.6 MB (100.00%)
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> 'int':
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]: return 0
        a = [[float('-inf') if obstacleGrid[j][i] else 0 for i in range(m)]
                for j in range(n)]
        a[0][0] = 1
        for k in range(1, n*m):
            j = k // m
            i = k % m
            if obstacleGrid[j][i]:
                a[j][i] = float('-inf')
            elif i == 0:
                a[j][i] = max(0, a[j-1][i])
            else:
                a[j][i] = max(0, a[j-1][i]) + max(0, a[j][i-1])
        return max(0, a[-1][-1])


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[0,0,0],
                  [0,1,0],
                  [0,0,0]]
        expected_output = 2
        output = Solution().uniquePathsWithObstacles(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [[0,1,0],
                  [0,1,0],
                  [0,0,0]]
        expected_output = 1
        output = Solution().uniquePathsWithObstacles(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [[1]]
        expected_output = 0
        output = Solution().uniquePathsWithObstacles(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
