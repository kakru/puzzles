#/usr/bin/env python3
import unittest

class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10: return n
        i = 0
        while True:
            subs = (9 * 10**i) * (i+1)
            if n > subs:
                n -= subs
                i += 1
            else:
                break
        number = (n-1)//(i+1) + 10**i
        digit = (n-1)%(i+1)
        return int(str(number)[digit])

# How to get a decimal digit from a number:
# digit = (number // 10**(which_one)) % 10
# this is counting from the last one, meaning 0=last digit, 1=one before the last one, etc.


class BasicTest(unittest.TestCase):
    def test_10(self):
        input_ = 10
        expected_output = 1
        output = Solution().findNthDigit(input_)
        self.assertEqual(output, expected_output)

    def test_11(self):
        input_ = 11
        expected_output = 0
        output = Solution().findNthDigit(input_)
        self.assertEqual(output, expected_output)

    def test_12(self):
        input_ = 12
        expected_output = 1
        output = Solution().findNthDigit(input_)
        self.assertEqual(output, expected_output)

    def test_13(self):
        input_ = 13
        expected_output = 1
        output = Solution().findNthDigit(input_)
        self.assertEqual(output, expected_output)

    def test_1000(self):
        input_ = 1000
        expected_output = 3
        output = Solution().findNthDigit(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)