#/usr/bin/env python3
import unittest

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = (2**31 - 1)
        INT_MIN = -(2**31)
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        s = str.strip()
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = -1
        else:
            sign = 1
        if s[0] in ('+', '-'):
            s = s[1:]
        number = 0
        for ch in s:
            if ch not in DIGITS:
                break
            else:
                number *= 10
                number += DIGITS.index(ch)
        number *= sign
        if number > INT_MAX:
            return INT_MAX
        elif number < INT_MIN:
            return INT_MIN
        else:
            return number



        


class BasicTest(unittest.TestCase):
    def test_m42(self):
        input_ = "-42"
        expected_output = -42
        output = Solution().myAtoi(input_)
        self.assertEqual(output, expected_output)

    def test_21893721783(self):
        input_ = "         2189372  sjfjkadjlfk"
        expected_output = 2189372
        output = Solution().myAtoi(input_)
        self.assertEqual(output, expected_output)

    def test_21893721783(self):
        input_ = " "
        expected_output = 0
        output = Solution().myAtoi(input_)
        self.assertEqual(output, expected_output)

    def test_m91283472332(self):
        input_ = "-91283472332"
        expected_output = -2147483648
        output = Solution().myAtoi(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)