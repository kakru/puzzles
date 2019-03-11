#/usr/bin/env python3
import unittest

# class Solution:  # TOO SLOW !!
#     def change(self, amount: 'int', coins: 'List[int]') -> 'int':
#         if amount == 0: return 1
#         if not coins: return 0
#         coins.sort(reverse=True)
#         def helper(amount, coin_index_start):
#             solutions = 0
#             if amount < coins[-1]: return 0
#             for i, coin in enumerate(coins[coin_index_start:], start=coin_index_start):
#                 if amount == coin:
#                     solutions += 1
#                 elif amount > coin:
#                     solutions += helper(amount - coin, i)
#             return solutions
#         return helper(amount, 0)

class Solution:  # 200 ms (56.67%)
    def change(self, amount: 'int', coins: 'List[int]') -> 'int':
        if amount == 0: return 1
        if not coins: return 0
        dp = [1] + [0] * amount
        for coin in coins:
            for a in range(1, amount+1):
                if a >= coin:
                    dp[a] += dp[a-coin]
        return dp[amount]


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 5, [1,2,5]
        expected_output = 4
        output = Solution().change(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 3, [2]
        expected_output = 0
        output = Solution().change(*input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 10, [10]
        expected_output = 1
        output = Solution().change(*input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = 6, [2,1]
        expected_output = 4
        output = Solution().change(*input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = 500, [3,5,7,8,9,10,11]
        expected_output = 35502874
        output = Solution().change(*input_)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main(verbosity=2)