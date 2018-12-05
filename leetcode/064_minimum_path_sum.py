#/usr/bin/env python3
import unittest

class Solution:
    def minPartialSum(self, m, n):
        if m == 1 and n == 1: return self.grid[0][0]
        if (m,n) not in self.cache:
            self.cache[(m,n)] = self.grid[m-1][n-1] + min(
                self.minPartialSum(m-1, n) if m > 1 else float('inf'),
                self.minPartialSum(m, n-1) if n > 1 else float('inf'))
        return self.cache[(m,n)]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.cache = {}
        return self.minPartialSum(len(grid), len(grid[0]))



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[1,3,1],
                  [1,5,1],
                  [4,2,1]]
        expected_output = 7
        output = Solution().minPathSum(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [[1,9,9],
                  [1,5,9],
                  [4,2,1]]
        expected_output = 9
        output = Solution().minPathSum(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):  # Time Limit Exceeded without cache
        input_ = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
        expected_output = 85
        output = Solution().minPathSum(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
