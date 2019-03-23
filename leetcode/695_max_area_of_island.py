#/usr/bin/env python3
import unittest
from typing import *

class Solution:  # 136 ms (22.80%)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        def findIsland():
            for y in range(n):
                if 1 in grid[y]: return (y, grid[y].index(1))
            return None
        def islandArea(y_start, x_start):
            stack = [(y_start, x_start)]
            grid[y_start][x_start] = 2
            size = 0
            while stack:
                y, x = stack.pop()
                size += 1
                for (j, i) in ((-1,0), (1,0), (0,-1), (0,1)):
                    if x+i < 0 or y+j < 0 or x+i >= m or y+j >= n: continue
                    if grid[y+j][x+i] == 1:
                        stack.append((y+j, x+i))
                        grid[y+j][x+i] = 2
            return size
        max_area_found = 0
        while True:
            i = findIsland()
            if not i: break
            i_area = islandArea(*i)
            if i_area > max_area_found:
                max_area_found = i_area
        return max_area_found


                        


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                  [0,0,0,0,0,0,0,1,1,1,0,0,0],
                  [0,1,1,0,1,0,0,0,0,0,0,0,0],
                  [0,1,0,0,1,1,0,0,1,0,1,0,0],
                  [0,1,0,0,1,1,0,0,1,1,1,0,0],
                  [0,0,0,0,0,0,0,0,0,0,1,0,0],
                  [0,0,0,0,0,0,0,1,1,1,0,0,0],
                  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        expected_output = 6
        output = Solution().maxAreaOfIsland(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [[0,0,0,0,0,0,0,0]]
        expected_output = 0
        output = Solution().maxAreaOfIsland(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [[1,1,0,0,0],
                  [1,1,0,0,0],
                  [0,0,0,1,1],
                  [0,0,0,1,1]]
        expected_output = 4
        output = Solution().maxAreaOfIsland(input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)