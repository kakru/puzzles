#/usr/bin/env python3
import unittest

class Solution:  # 36 ms (100.00%) - naive but fast solution, enough for the contest
    def bitwiseComplement(self, N: 'int') -> 'int':
        return int(bin(N)[2:].replace("1", "2").replace("0", "1").replace("2", "0"), 2)


class BasicTest(unittest.TestCase):

    def test_all(self):
        for test in [
            [1, 0],
            [5, 2],
            [7, 0],
            [10, 5],
            [3, 0],
        ]:
            self.assertEqual(Solution().bitwiseComplement(test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)