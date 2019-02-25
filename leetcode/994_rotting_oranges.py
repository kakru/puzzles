#/usr/bin/env python3
import unittest

from collections import deque
class Solution:  # 56 ms (37.29%)
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        size_y = len(grid)
        if size_y == 0: return 0
        size_x = len(grid[0])
        # count oranges
        rotten = fresh = 0
        rotten_set = set()
        for y, row in enumerate(grid):
            rotten += row.count(2)
            fresh += row.count(1)
            for x, orange in enumerate(row):
                if orange == 2:
                    rotten_set.add((y, x))
        if fresh == 0: return 0  # everything already rotten
        if rotten == 0: return -1  # nothing rotten
        q = deque([(f, 0) for f in rotten_set])
        while q:
            p, time = q.popleft()
            for (j, i) in ((-1,0), (1,0), (0,-1), (0,1)):
                if size_y > p[0]+j >= 0 and size_x > p[1]+i >= 0 and grid[p[0]+j][p[1]+i] == 1:
                    grid[p[0]+j][p[1]+i] = 2
                    fresh -= 1
                    q.append(((p[0]+j, p[1]+i), time+1))        
        if fresh > 0:
            return -1
        else:
            return time


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[2,1,1],[1,1,0],[0,1,1]]
        expected_output = 4
        output = Solution().orangesRotting(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [[2,1,1],[0,1,1],[1,0,1]]
        expected_output = -1
        output = Solution().orangesRotting(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [[0,2]]
        expected_output = 0
        output = Solution().orangesRotting(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):  # do not assume the grid to be a sqare
        input_ = [[1],[2]]
        expected_output = 1
        output = Solution().orangesRotting(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
