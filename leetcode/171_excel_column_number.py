import unittest

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        column = 0
        for pos, letter in enumerate(reversed(s)):
            column += (ord(letter) - 64) * 26**pos
        return column        
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 'A'
        expected_output = 1
        output = Solution().titleToNumber(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 'AB'
        expected_output = 28
        output = Solution().titleToNumber(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 'ZY'
        expected_output = 701
        output = Solution().titleToNumber(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)