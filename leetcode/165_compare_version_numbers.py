#/usr/bin/env python3
import unittest

from itertools import zip_longest
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = (int(x) for x in version1.split("."))
        ver2 = (int(x) for x in version2.split("."))
        for v1, v2 in zip_longest(ver1, ver2, fillvalue=0):
            if v1 == v2:
                continue
            elif v1 > v2:
                return 1
            else:
                return -1
        return 0


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "0.1", "1.1"
        expected_output = -1
        output = Solution().compareVersion(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "1.0.1", "1"
        expected_output = 1
        output = Solution().compareVersion(*input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = "1.01", "1.001"
        expected_output = 0
        output = Solution().compareVersion(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)




