#/usr/bin/env python3
import unittest

from itertools import permutations
class Solution:  # 40 ms (76.92%)
    def largestTimeFromDigits(self, A: 'List[int]') -> 'str':
        best = ""
        for h1, h2, m1, m2 in permutations(A):
            if 10*h1+h2 < 24 and 10*m1+m2 < 60:
                time = "{}{}:{}{}".format(h1, h2, m1, m2)
                if not best or time > best:
                    best = time
        return best

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,3,4]
        expected_output = "23:41"
        output = Solution().largestTimeFromDigits(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1,1,1,1]
        expected_output = "11:11"
        output = Solution().largestTimeFromDigits(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [5,1,5,5]
        expected_output = "15:55"
        output = Solution().largestTimeFromDigits(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [5,5,5,5]
        expected_output = ""
        output = Solution().largestTimeFromDigits(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = [2,0,6,6]
        expected_output = "06:26"
        output = Solution().largestTimeFromDigits(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)