#/usr/bin/env python3
import unittest

class Solution:  # 88 ms (27.13%)
    def maxProfit(self, prices):
        size = len(prices)
        if size == 0: return 0
        # first buy&sell
        P_until = [0]  # best buy&sell before or on the i-th day
        min_so_far = prices[0]
        profit_max = 0
        for i, v in enumerate(prices[1:], start=1):
            min_so_far = min(min_so_far, v)
            profit_max = max(v - min_so_far, profit_max)
            P_until.append(profit_max)
        # second buy&sell
        P_from = [0] * size  # best buy&sell starting on the i-th day
        max_so_far = prices[-1]
        profit_max = 0
        for i in range(1, size+1):
            # selling on i-th day from the last one (-1 = last day)
            max_so_far = max(max_so_far, prices[-i])
            profit_max = max(max_so_far - prices[-i], profit_max)
            P_from[-i] = profit_max
        # simulate two buy&sell pairs -> until i-th day + after i-th day
        result = 0
        for i in range(1, size):
            result = max(result, P_until[i] + P_from[i])
        return result


class BasicTest(unittest.TestCase):
    def test_0(self):
        input_ = []
        expected_output = 0
        output = Solution().maxProfit(input_)
        self.assertEqual(output, expected_output)

    def test_1(self):
        input_ = [3,3,5,0,0,3,1,4]
        expected_output = 6
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
