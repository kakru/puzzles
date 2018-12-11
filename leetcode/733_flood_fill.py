#/usr/bin/env python3
import unittest


class Solution:  # 136ms, best LeetCode solution ~60ms
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        image_h = len(image)
        image_w = len(image[0])
        q = [(sr, sc)]
        color = image[sr][sc]
        # track visited pixels to avoid loops
        visited = [[False]*image_w for _ in range(image_h)]
        while q:
            p = q.pop()
            visited[p[0]][p[1]] = True
            q.extend([ (p[0]+i, p[1]+j)
                for (i, j) in ((-1,0), (1, 0), (0, -1), (0, 1))
                if 0 <= p[0]+i < image_h 
                and 0 <= p[1]+j < image_w
                and image[p[0]+i][p[1]+j] == color
                and not visited[p[0]+i][p[1]+j] ])
            image[p[0]][p[1]] = newColor
        return image



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2
        expected_output = [[2,2,2],[2,2,0],[2,0,1]]
        output = Solution().floodFill(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [[0,0,0],[0,1,1]], 1, 1, 1
        expected_output = [[0,0,0],[0,1,1]]
        output = Solution().floodFill(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
