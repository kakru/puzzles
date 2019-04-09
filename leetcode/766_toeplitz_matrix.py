#/usr/bin/env python3
import unittest


class Solution:
    def isToeplitzMatrix(self, matrix):
        row_count, col_count = len(matrix), len(matrix[0])
        if row_count == 1 or col_count == 1: return True
        for row_nr in range(1, row_count):
            for col_nr in range(1, col_count):
                if matrix[row_nr][col_nr] != matrix[row_nr-1][col_nr-1]:
                    return False
        return True



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[1,2,3,4],
                  [5,1,2,3],
                  [9,5,1,2]]
        expected_output = True
        output = Solution().isToeplitzMatrix(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [[1,2],
                  [2,2]]
        expected_output = False
        output = Solution().isToeplitzMatrix(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [[18],
                  [66]]
        expected_output = True
        output = Solution().isToeplitzMatrix(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [[11,74,0,93],[40,11,74,7]]
        expected_output = False
        output = Solution().isToeplitzMatrix(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)