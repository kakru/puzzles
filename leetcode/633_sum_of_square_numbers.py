#/usr/bin/env python3
import unittest

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        sqs = [i**2 for i in range(int(c ** (0.5) // 1) + 1)]
        seen = set()
        for i in sqs:
            if 2*i == c or c - i in seen:
                return True
            else:
                seen.add(i)
        return False
        


class BasicTest(unittest.TestCase):
    def test_5(self):
        input_ = 5
        expected_output = True
        output = Solution().judgeSquareSum(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 3
        expected_output = False
        output = Solution().judgeSquareSum(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 2
        expected_output = True
        output = Solution().judgeSquareSum(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
