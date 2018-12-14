#/usr/bin/env python3
import unittest

from itertools import combinations
class Solution:  # O(N^3) but it's only up to 50 points, so good enough
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p1, p2, p3):
            return 0.5 * abs(p1[0]*(p2[1]-p3[1]) + 
                             p2[0]*(p3[1]-p1[1]) +
                             p3[0]*(p1[1]-p2[1]))
        return max(area(*c) for c in combinations(points, 3))


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[0,0],[0,1],[1,0],[0,2],[2,0]]
        expected_output = 2
        output = Solution().largestTriangleArea(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
