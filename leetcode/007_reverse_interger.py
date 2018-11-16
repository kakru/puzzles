#/usr/bin/env python3
import unittest

# class Solution:  # v1
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         if x == 0:
#             return 0
#         elif x < 0:
#             sign = -1
#             x *= sign
#         else:
#             sign = 1
#         digits = []
#         while x > 0:
#             digit = x % 10
#             digits.append(digit)
#             x //= 10
#         number = 0
#         for digit in digits:
#             number += digit
#             number *= 10
#         number //=10
#         return sign*number

class Solution:  # v2 - after removing the array for storing digits
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or -(2**31) > x >= 2**31:
            return 0
        elif x < 0:
            sign = -1
            x *= sign
        else:
            sign = 1
        y = 0
        while x > 0:
            digit = x % 10
            y += digit
            x //= 10
            y *= 10
        y //=10
        y *= sign
        if abs(y) < (2**31):
            return y
        else:
            return 0


                    
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 123
        expected_output = 321
        output = Solution().reverse(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = -123
        expected_output = -321
        output = Solution().reverse(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 120
        expected_output = 21
        output = Solution().reverse(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 1534236469
        expected_output = 0
        output = Solution().reverse(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)