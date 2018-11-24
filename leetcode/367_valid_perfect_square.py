#/usr/bin/env python3
import unittest

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return True
        left, right = 1, num
        while right-left > 1:
            check = (left+right)//2
            if check**2 > num:
                right = check
            elif check**2 < num:
                left = check
            else:
                return True
        return False


class BasicTest(unittest.TestCase):
    def test_16(self):
        input_ = 16
        expected_output = True
        output = Solution().isPerfectSquare(input_)
        self.assertEqual(output, expected_output)

    def test_14(self):
        input_ = 14
        expected_output = False
        output = Solution().isPerfectSquare(input_)
        self.assertEqual(output, expected_output)

    def test_10xx(self):
        input_ = 10000000000001
        expected_output = False
        output = Solution().isPerfectSquare(input_)
        self.assertEqual(output, expected_output)

    def test_10xx0(self):
        input_ = 1000000000000
        expected_output = True
        output = Solution().isPerfectSquare(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)