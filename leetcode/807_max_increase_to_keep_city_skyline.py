#/usr/bin/env python3
import unittest

class Solution:  # 76ms solution (mine)
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid_height = len(grid)
        grid_width = len(grid[0])
        added = [[0]*grid_width for i in range(grid_height)]
        left = [max(grid[x]) for x in range(grid_height)]
        top = [max([grid[y][x] for y in range(grid_height)]) for x in range(grid_width)]
        for y in range(grid_height):
            for x in range(grid_width):
                added[y][x] = min(left[y], top[x]) - grid[y][x]
        return sum([sum(added[row]) for row in range(grid_height)])

# class Solution:  # 44 ms (the best submitted solution)
#     def maxIncreaseKeepingSkyline(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         totalSum = 0
#         maxCol = [max(col) for col in zip(*grid)]
#         maxRow = [max(row) for row in grid]
#         for x, row in enumerate(grid):
#             for y, sqr in enumerate(row):
#                 sqrHeight = min( maxCol[y], maxRow[x] )
#                 sqrSum = sqrHeight - sqr
#                 totalSum += sqrSum 
#         return totalSum



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
        expected_output = 35
        output = Solution().maxIncreaseKeepingSkyline(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)