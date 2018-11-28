#/usr/bin/env python3
import unittest

# There are more pretty solutions on LeetCode
# In principle without 2 arrays, casue anyway we don't need them

from collections import defaultdict
class Solution:
    @staticmethod
    def emptyTriangle(size):
        return [[0.0]*i for i in range(1,size+2)]
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        accu = self.emptyTriangle(query_row)
        over = self.emptyTriangle(query_row)
        accu[0][0] = min(1.0, poured)
        over[0][0] = poured - accu[0][0]
        for i in range(1, query_row+1):
            for j in range(i):
                if j>0:
                    accu[i][j] = accu[i][~j] = 0.5 * (over[i-1][j-1] + over[i-1][j])
                else:
                    accu[i][j] = accu[i][~j] = 0.5 * over[i-1][j]
                if accu[i][j] > 1.0:
                    over[i][j] = over[i][~j] = accu[i][j] - 1.0
                    accu[i][j] = accu[i][~j] = 1.0
        return accu[query_row][query_glass]


class BasicTest(unittest.TestCase):
    def test_1(self):
        poured = 1
        query_glass = 1
        query_row = 1
        expected_output = 0.0
        output = Solution().champagneTower(poured, query_row, query_glass)
        self.assertEqual(output, expected_output)

    def test_2(self):
        poured = 2
        query_glass = 1
        query_row = 1
        expected_output = 0.5
        output = Solution().champagneTower(poured, query_row, query_glass)
        self.assertEqual(output, expected_output)

    def test_3_middle(self):
        poured = 3
        query_glass = 1
        query_row = 1
        expected_output = 1.0
        output = Solution().champagneTower(poured, query_row, query_glass)
        self.assertEqual(output, expected_output)

    def test_3(self):
        poured = 4
        query_glass = 1
        query_row = 2
        expected_output = 0.5
        output = Solution().champagneTower(poured, query_row, query_glass)
        self.assertEqual(output, expected_output)

    def test_4(self):
        poured = 4
        query_row = 1
        query_glass = 0
        expected_output = 1.0
        output = Solution().champagneTower(poured, query_row, query_glass)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)