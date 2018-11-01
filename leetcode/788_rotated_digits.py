#!/usr/bin/env python3
import unittest

# this solution is 208ms, the best submission = 32ms,
# by generating only the good numbers, and not by
# generating all of them and counting good
class Solution:
    @staticmethod
    def getDigits(number):
        digits = set()
        while number:
            digit = number % 10
            digits.add(digit)
            number //= 10
        return digits

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        bad_digits = set([3,4,7])
        good_digits = set([2,5,6,9])
        good_counter = 0
        for number in range(1, N+1):
            digits = self.getDigits(number)
            if any(digits.intersection(good_digits)) and not any(digits.intersection(bad_digits)):
                good_counter += 1
        return good_counter
            
                  
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 10
        expected_output = 4
        output = Solution().rotatedDigits(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 1
        expected_output = 0
        output = Solution().rotatedDigits(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 10000
        expected_output = 2320  # no idea
        output = Solution().rotatedDigits(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = 2
        expected_output = 1
        output = Solution().rotatedDigits(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)