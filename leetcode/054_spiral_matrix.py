#/usr/bin/env python3
import unittest

# version 1
class Solution:  # 36 ms (51.51%), memory 13.2 MB (5.18%)
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        def spiral(matrix, y1, y2, x1, x2):  # matrix[y1:y2][x1:x2] not working as expected without numpy
            size_y = y2 - y1
            size_x = x2 - x1
            if size_y == 0 or size_x == 0: return []
            elif size_y == 1: return [matrix[y1][i] for i in range(x1, x2)]
            elif size_x == 1: return [matrix[i][x1] for i in range(y1, y2)]
            result = []
            for x in range(x1, x2):  # go right
                result.append(matrix[y1][x])
            for y in range(y1+1, y2):  # go down
                result.append(matrix[y][x2-1])
            for x in range(x2-2, x1-1, -1):  # go left
                result.append(matrix[y2-1][x])
            for y in range(y2-2, y1, -1):  # go up
                result.append(matrix[y][x1])
            smaller = spiral(matrix, y1+1, y2-1, x1+1, x2-1)
            result.extend(smaller)
            return result
        if len(matrix) == 0: return []
        return spiral(matrix, 0, len(matrix), 0, len(matrix[0]))

# version 2
class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if len(matrix) == 0: return []
        def spiral(matrix, y1, y2, x1, x2):  # matrix[y1:y2][x1:x2] not working as expected without numpy
            size_y = y2 - y1
            size_x = x2 - x1
            if size_y == 0 or size_x == 0: return []
            elif size_y == 1: return [matrix[y1][i] for i in range(x1, x2)]
            elif size_x == 1: return [matrix[i][x1] for i in range(y1, y2)]
            result = []
            for x in range(x1, x2):  # go right
                result.append(matrix[y1][x])
            for y in range(y1+1, y2):  # go down
                result.append(matrix[y][x2-1])
            for x in range(x2-2, x1-1, -1):  # go left
                result.append(matrix[y2-1][x])
            for y in range(y2-2, y1, -1):  # go up
                result.append(matrix[y][x1])
            return result
        result = spiral(matrix, 0, len(matrix), 0, len(matrix[0]))
        for k in range(1, min(len(matrix), len(matrix[0]))):
            result.extend(spiral(matrix, k, len(matrix)-k, k, len(matrix[0])-k))
        return result


class BasicTest(unittest.TestCase):
    def test_6(self):
        input_ = [[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11,12,13,14,15],
                  [16,17,18,19,20],
                  [21,22,23,24,25]]
        expected_output = [1,2,3,4,5, 10,15,20,25, 24,23,22,21, 16,11,6, 7,8,9, 14,19, 18,17 ,12 ,13]
        output = Solution().spiralOrder(input_)
        self.assertEqual(output, expected_output)

    def test_1(self):
        input_ = [[ 1, 2, 3 ],
                  [ 4, 5, 6 ],
                  [ 7, 8, 9 ]]
        expected_output = [1,2,3,6,9,8,7,4,5]
        output = Solution().spiralOrder(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [[ 1, 2, 3, 4, 5 ],
                  [ 10, 9, 8, 7, 6 ]]
        expected_output = [1,2,3,4,5,6,7,8,9,10]
        output = Solution().spiralOrder(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
        expected_output = [1,2,3,4,5,6,7,8,9,10]
        output = Solution().spiralOrder(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
        expected_output = [1,11,12,13,14,15,16,17,18,19,20,10,9,8,7,6,5,4,3,2]
        output = Solution().spiralOrder(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = [[1,  2, 3, 4],
                  [5,  6, 7, 8],
                  [9, 10,11,12],
                  [13,14,15,16]]
        expected_output = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
        output = Solution().spiralOrder(input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)
