#/usr/bin/env python3
import unittest

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        counter = 0
        while i >= 0 and s[i] != ' ':
            i -= 1
            counter += 1
        return counter            
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 'Hello World'
        expected_output = 5
        output = Solution().lengthOfLastWord(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 'a '
        expected_output = 1
        output = Solution().lengthOfLastWord(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = ' a'
        expected_output = 1
        output = Solution().lengthOfLastWord(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = '  '
        expected_output = 0
        output = Solution().lengthOfLastWord(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)