#/usr/bin/env python3
import unittest
from typing import *

        
class Solution:  # 52 ms (12.74%)
    def wordPattern(self, pattern: str, str: str) -> bool:
        def convert(words):
            nxt, d = 97, {}
            result = []
            for word in words:
                if word not in d:
                    d[word] = chr(nxt)
                    nxt += 1
                result.append(d[word])
            return result
        return convert(pattern) == convert(str.split(" "))



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "abba", "dog cat cat dog"
        expected_output = True
        output = Solution().wordPattern(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "e", "eureka"
        expected_output = True
        output = Solution().wordPattern(*input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = "aba", "cat cat cat dog"
        expected_output = False
        output = Solution().wordPattern(*input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = "abba", "dog cat cat fish"
        expected_output = False
        output = Solution().wordPattern(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)