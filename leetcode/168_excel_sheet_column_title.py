#/usr/bin/env python3
import unittest

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...

# Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Excel Sheet Column Title.
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        column = []
        while n > 0:
            letter = n % 26 or 26
            column.append(chr(64 + letter))
            n = (n-letter) // 26
        return "".join(reversed(column))


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 1
        expected_output = "A"
        output = Solution().convertToTitle(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 2
        expected_output = "B"
        output = Solution().convertToTitle(input_)
        self.assertEqual(output, expected_output)

    def test_25(self):
        input_ = 25
        expected_output = "Y"
        output = Solution().convertToTitle(input_)
        self.assertEqual(output, expected_output)

    def test_26(self):
        input_ = 26
        expected_output = "Z"
        output = Solution().convertToTitle(input_)
        self.assertEqual(output, expected_output)

    def test_27(self):
        input_ = 27
        expected_output = "AA"
        output = Solution().convertToTitle(input_)
        self.assertEqual(output, expected_output)

    def test_28(self):
        input_ = 28
        expected_output = "AB"
        output = Solution().convertToTitle(input_)
        self.assertEqual(output, expected_output)

    def test_701(self):
        input_ = 701
        expected_output = "ZY"
        output = Solution().convertToTitle(input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)
