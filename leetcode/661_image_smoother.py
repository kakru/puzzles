#/usr/bin/env python3
import unittest

class Solution:  # First approach: 864ms
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def nbr(y, x, max_y, max_x):
            res = []
            if y > 0:
                if x > 0: res.append(M[y-1][x-1])
                if x < max_x-1: res.append(M[y-1][x+1])
                res.append(M[y-1][x])
            if y < max_y-1:
                if x > 0: res.append(M[y+1][x-1])
                if x < max_x-1: res.append(M[y+1][x+1])
                res.append(M[y+1][x])
            if x > 0: res.append(M[y][x-1])
            if x < max_x-1: res.append(M[y][x+1])
            res.append(M[y][x])
            return res
        def avg(a):
            return sum(a)//len(a)
        size_y = len(M)
        if size_y == 0: return M
        size_x = len(M[0])
        return [[avg(nbr(y, x, size_y, size_x))
            for x in range(size_x)]
            for y in range(size_y)]


class Solution:  # Simplified approach: 1124ms
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        size_y = len(M)
        if size_y == 0: return M
        size_x = len(M[0])
        s = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)]
        def smooth(y, x):
            r = [ M[y+i][x+j] for i, j in s if 0 <= y+i < size_y and 0 <= x+j < size_x ]
            return sum(r)//len(r)
        return [ [smooth(y, x) for x in range(size_x)] for y in range(size_y) ]
                
        


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[1,1,1],
                  [1,0,1],
                  [1,1,1]]
        expected_output = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
        output = Solution().imageSmoother(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
