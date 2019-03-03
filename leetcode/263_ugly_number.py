#/usr/bin/env python3
import unittest

class Solution:
    def isUgly(self, num: 'int') -> 'bool':
        if num <= 0: return False
        while num % 5 == 0: num /= 5
        while num % 3 == 0: num /= 3
        while num % 2 == 0: num /= 2
        return num == 1


class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            [6, True],
            [14, False],
            [8, True],
        ]:
            self.assertEqual(Solution().isUgly(test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)