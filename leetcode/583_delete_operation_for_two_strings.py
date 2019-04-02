#/usr/bin/env python3
import unittest
from typing import *

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        elif not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2+1) for _ in range(len1+1)]
        for i in range(len1+1):
            for j in range(len2+1):
                if i == 0 or j == 0:
                    dp[i][j] = i+j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "sea", "eat"
        expected_output = 2
        output = Solution().minDistance(*input_)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main(verbosity=2)