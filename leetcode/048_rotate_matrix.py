import unittest

"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""


class SolutionNotInPlace:  # not in place
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        new_m = [[None for x in range(size)] for y in range(size)]
        for i in range(size):
            for j in range(size):
                new_m[j][size-1-i] = matrix[i][j]
        for i in range(size):
            for j in range(size):
                matrix[i][j] = new_m[i][j]
        print(new_m)


class Solution1:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for lvl in range(size//2):
            bar1 = [(lvl, x) for x in range(lvl+1, size-lvl)]  # top
            bar2 = [(y, size-lvl-1) for y in range(lvl+1, size-lvl)]  # right
            bar3 = [(~lvl, ~x) for x in range(lvl+1, size-lvl)]  # top
            bar4 = [(~y, ~(size-lvl-1)) for y in range(lvl+1, size-lvl)]  # right
            for i in range(len(bar1)):
                t1y, t1x = bar1[i]
                t2y, t2x = bar2[i]
                t3y, t3x = bar3[i]
                t4y, t4x = bar4[i]
                matrix[t2y][t2x], matrix[t3y][t3x], matrix[t4y][t4x], matrix[t1y][t1x] = \
                matrix[t1y][t1x], matrix[t2y][t2x], matrix[t3y][t3x], matrix[t4y][t4x]


class Solution2:  # The best LeetCode solution
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution3:
    def rotate(self, A):
        A[:] = zip(*A[::-1])


class Solution4:
    def rotate(self, A):
        n = len(A)
        for i in range(n//2):
            for j in range(n-n//2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = A[~j][i], A[~i][~j], A[j][~i], A[i][j]


Solution = Solution4


class Tests(unittest.TestCase):
    def test_3x3(self):
        input_ = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        expected_output = [
            [7,4,1],
            [8,5,2],
            [9,6,3]
        ]
        Solution().rotate(input_)
        self.assertEqual(expected_output, input_)

    def test_4x4(self):
        input_ = [
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]
        ]
        expected_output = [
            [15,13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7,10,11]
        ]
        Solution().rotate(input_)
        self.assertEqual(expected_output, input_)

    def test_5x5(self):
        input_ = [
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]
        ]
        expected_output = [
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]
        ]
        Solution().rotate(expected_output)
        Solution().rotate(input_)
        self.assertEqual(expected_output, input_)


unittest.main(verbosity=2)
