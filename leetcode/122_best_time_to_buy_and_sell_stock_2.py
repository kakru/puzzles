#/usr/bin/env python3
import unittest

class Solution:
    def maxProfit(self, prices):
        i, size = 1, len(prices)
        profit = 0
        while i < size:
            while i < size and prices[i-1] >= prices[i]: i += 1
            buy = prices[i-1]
            while i < size and prices[i-1] <= prices[i]: i += 1
            profit += prices[i-1] - buy
        return profit


class BasicTest(unittest.TestCase):
    def test_0(self):
        input_ = []
        expected_output = 0
        output = Solution().maxProfit(input_)
        self.assertEqual(output, expected_output)

    def test_1(self):
        input_ = [7,1,5,3,6,4]
        expected_output = 7
        output = Solution().maxProfit(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1,2,3,4,5]
        expected_output = 4
        output = Solution().maxProfit(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [7,6,4,3,1]
        expected_output = 0
        output = Solution().maxProfit(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)