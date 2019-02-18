#/usr/bin/env python3
import unittest

# class Solution:
#     def maxProfit(self, prices):  # brute force
#         size = len(prices)
#         max_profit = 0
#         for buy_day in range(size-1):  # cannot buy on the last day
#             for sell_day in range(buy_day+1, size):
#                 max_profit = max(max_profit, prices[sell_day] - prices[buy_day])
#         return max_profit

# class Solution:
#     def maxProfit(self, prices):  # remove repreated prices first, 7796 ms (very slow)
#         if not prices: return 0
#         new_prices = [prices[0]]
#         for i in range(1, len(prices)):
#             if prices[i-1] != prices[i]: new_prices.append(prices[i])
#         prices = new_prices
#         size = len(prices)
#         max_profit = 0
#         for buy_day in range(size-1):  # cannot buy on the last day
#             for sell_day in range(buy_day+1, size):
#                 max_profit = max(max_profit, prices[sell_day] - prices[buy_day])
#         return max_profit

class Solution:  # 48 ms, (faster than 61.85%), 13.6 MB (less than 100%)
    def maxProfit(self, prices):
        size = len(prices)
        if not size: return 0
        maximum_after = [0] * size
        # generate max(prices[i+1:]) for each index of prices
        maximum = 0
        for i in range(1, size):
            maximum = maximum_after[-i-1] = max(maximum, prices[-i])
        profits = []
        for i in range(size):
            profits.append(maximum_after[i] - prices[i])
        profits.append(0)
        return max(profits)


class Solution:
    def maxProfit(self, prices):  # 44 ms, (faster than 84.48%), 13 MB (less than 100%)
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


class BasicTest(unittest.TestCase):
    def test_0(self):
        input_ = []
        expected_output = 0
        output = Solution().maxProfit(input_)
        self.assertEqual(output, expected_output)

    def test_1(self):
        input_ = [7,1,5,3,6,4]
        expected_output = 5
        output = Solution().maxProfit(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [7,6,4,3,1]
        expected_output = 0
        output = Solution().maxProfit(input_)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main(verbosity=2)