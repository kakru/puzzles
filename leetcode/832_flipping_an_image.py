import unittest
from math import ceil

class Solution:  # 56 ms improved to 52 ms
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        size = len(A)
        for line in range(size):
            for column in range(int(size/2)):
                # A[line][column], A[line][-column-1] = abs(A[line][-column-1]-1), abs(A[line][column]-1)
                A[line][column], A[line][~column] = A[line][~column]^1, A[line][column]^1
            if size % 2:
                # A[line][int(size/2)] = abs(A[line][int(size/2)]-1)
                A[line][int(size/2)] = A[line][int(size/2)]^1
        return A
                
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[1,1,0],[1,0,1],[0,0,0]]
        expected_output = [[1,0,0],[0,1,0],[1,1,1]]
        output = Solution().flipAndInvertImage(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
        expected_output = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
        output = Solution().flipAndInvertImage(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)