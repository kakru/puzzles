#/usr/bin/env python3
import unittest

class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:K]
        


class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            [([[1,3],[-2,2]], 1), [[-2,2]]],
        ]:
            self.assertEqual(Solution().kClosest(*test[0]), test[1])


if __name__ == '__main__':
    unittest.main(verbosity=2)
