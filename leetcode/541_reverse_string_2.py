#/usr/bin/env python3
import unittest

class Solution:
    def reverseStr(self, s: 'str', k: 'int') -> 'str':
        size = len(s)
        if size < 2: return s
        S = list(s)  # let's assume that strings are mutable (list of chars instead)
        for i in range(0, size, 2*k):
            S[i:i+k] = reversed(S[i:i+k])
        return "".join(S)


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "abcdefg", 2
        expected_output = "bacdfeg"
        output = Solution().reverseStr(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "abcdefg", 8
        expected_output = "gfedcba"
        output = Solution().reverseStr(*input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)