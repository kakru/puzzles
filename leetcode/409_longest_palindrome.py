#/usr/bin/env python3
import unittest

from collections import Counter
class Solution:  # 40 ms (69.37%)
    def longestPalindrome(self, s: 'str') -> 'int':
        pairs = 0
        orphan = 0
        for _, c in Counter(s).most_common():
            pairs += c // 2
            if not orphan and c % 2: orphan = 1
        return 2*pairs + orphan


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "abccccdd"
        expected_output = 7
        output = Solution().longestPalindrome(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)