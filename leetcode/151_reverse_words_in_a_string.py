#/usr/bin/env python3
import unittest

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(s.split()))

# Is it possible to solve it in-place in O(1) space (assuming the code is in C)?


class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            ["the sky is blue", "blue is sky the"],
            ["   a   b ", "b a"]
        ]:
            self.assertEqual(Solution().reverseWords(test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)
