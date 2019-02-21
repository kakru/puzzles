#/usr/bin/env python3
import unittest

"""Given an integer, write a function to determine if it is a power of two."""


class Solution:  # 48 ms
    def isPowerOfTwo(self, n: 'int') -> 'bool':
        if n == 0: return False
        return bool(n & n-1 == 0)
        

class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            [0, False],
            [1, True],
            [2, True],
            [3, False],
        ]:
            self.assertEqual(Solution().isPowerOfTwo(test[0]), test[1])


if __name__ == '__main__':
    unittest.main(verbosity=2)