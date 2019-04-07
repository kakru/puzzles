import unittest
from typing import *

# can be solved easily as DFS.
# I decided to go with a primitive union-find, which end up being slow

from collections import defaultdict
class Solution:  # 428 ms (5.07%), very slow...
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        # create union-find
        groups = defaultdict(set)
        groups_count = 0
        def union(g1, g2):
            if groups[g1] is groups[g2]: return 0
            # order g1, g2 by length -> len(g1) <= len(g2)
            g1, g2 = (g1, g2) if len(groups[g1])<=len(groups[g2]) else (g2, g1)
            groups[g2] = groups[g2].union(groups[g1])
            for g in groups[g2]: groups[g] = groups[g2]
            return 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    groups[m*i + j].add(m*i + j)
                    groups_count += 1
        if groups_count == 0: return 0
        # process union-find
        for g in groups.keys():
            y, x = divmod(g, m)
            for (i, j) in ((-1,0), (1,0), (0,-1), (0,1)):
                if 0 <= y+i < n and 0 <= x+j < m and grid[y+i][x+j] == "1":
                    groups_count -= union(g, m*(y+i)+(x+j))
        return groups_count


# LeetCode - clever submission:
# def numIslands(self, grid):
#     def sink(i, j):
#         if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
#             grid[i][j] = '0'
#             map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
#             return 1
#         return 0
#     return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i]))) 


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = """11110
                    11010
                    11000
                    00000""".replace(" ", "").split("\n")
        expected_output = 1
        output = Solution().numIslands(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = """11000
                    11000
                    00100
                    00011""".replace(" ", "").split("\n")
        expected_output = 3
        output = Solution().numIslands(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = """10000
                    11000
                    00000
                    00000""".replace(" ", "").split("\n")
        expected_output = 1
        output = Solution().numIslands(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)