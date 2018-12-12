#/usr/bin/env python3
import unittest

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x = bin(n)[:1:-1]
        return int(x + '0'*(32-len(x)), 2)


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 43261596
        expected_output = 964176192
        output = Solution().reverseBits(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
