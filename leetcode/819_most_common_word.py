#/usr/bin/env python3
import unittest

import string
from collections import Counter
class Solution:  # 40 ms (75.78%)
    def mostCommonWord(self, paragraph: 'str', banned: 'List[str]') -> 'str':
        paragraph = paragraph.translate(
            str.maketrans(string.punctuation,
            ' '*len(string.punctuation))).lower()
        for word, _ in Counter(paragraph.split()).most_common():
            if word not in banned:
                return word


class BasicTest(unittest.TestCase):
    def test_1(self):
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        expected_output = "ball"
        output = Solution().mostCommonWord(paragraph, banned)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)