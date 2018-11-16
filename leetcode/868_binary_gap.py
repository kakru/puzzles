#/usr/bin/env python3
import unittest

class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        # to check if the first (most right-side) bit is set we use: n&1
        #
        # we iterate over bits from right to left in the number
        # 1. lt's find the first 1
        while N > 0 and not N&1:
            N >>= 1
        # 2. if it's the only 1, return
        if N == 1:
            return 0
        # 3. look for the most distant 1s
        max_distance = distance = 0
        while N > 1:
            b = N&1
            if not b:
                distance += 1
            else:
                distance = 0
            N >>= 1
            max_distance = max(distance, max_distance)
        return max_distance+1
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 22
        expected_output = 2
        output = Solution().binaryGap(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 5
        expected_output = 2
        output = Solution().binaryGap(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 6
        expected_output = 1
        output = Solution().binaryGap(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = 8
        expected_output = 0
        output = Solution().binaryGap(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = 13
        expected_output = 2
        output = Solution().binaryGap(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)