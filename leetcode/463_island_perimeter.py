import unittest

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        perim = 0
        for j, y in enumerate(grid):
            for i, x in enumerate(y):
                if x == 1:
                    perim += 4
                    if j>0 and grid[j-1][i]:  # top
                        perim -= 1
                    if j<height-1 and grid[j+1][i]:  # bottom
                        perim -= 1
                    if i>0 and grid[j][i-1]:  # left
                        perim -= 1
                    if i<width-1 and grid[j][i+1]:  # right
                        perim -= 1
        return perim

                   
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[0,1,0,0],
                  [1,1,1,0],
                  [0,1,0,0],
                  [1,1,0,0]]
        expected_output = 16
        output = Solution().islandPerimeter(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [[0,1,0,0],
                  [0,1,0,0],
                  [0,1,0,0],
                  [0,1,0,0]]
        expected_output = 10
        output = Solution().islandPerimeter(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [[0,0,0,0],
                  [0,1,0,0],
                  [0,1,0,0],
                  [0,0,0,0]]
        expected_output = 6
        output = Solution().islandPerimeter(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [[0,0,0,0],
                  [0,0,0,0],
                  [0,1,0,0],
                  [0,0,0,0]]
        expected_output = 4
        output = Solution().islandPerimeter(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = [[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]]
        expected_output = 16
        output = Solution().islandPerimeter(input_)
        self.assertEqual(output, expected_output)

    def test_6(self):
        input_ = [[1,1,1,1],
                  [0,0,0,1],
                  [1,1,1,1],
                  [1,0,0,0]]
        expected_output = 22
        output = Solution().islandPerimeter(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)