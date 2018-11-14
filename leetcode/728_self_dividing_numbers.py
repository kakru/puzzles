#/usr/bin/env python3
import unittest

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right+1):
            digits = [int(x) for x in str(i)]
            if not(0 in digits or any(i%digit for digit in digits)):
                result.append(i)
        return result


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 1, 22
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        output = Solution().selfDividingNumbers(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)