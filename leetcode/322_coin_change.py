#/usr/bin/env python3
import unittest


class Solution:  # 1256 ms (60.03%), 12.6 MB (100.00%)
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        solutions = [float('inf')] * (amount + 1)
        solutions[0] = 0
        coins_s = sorted(coins)
        for i in range(1, amount+1):
            for c in coins_s:
                if c > i: continue
                solutions[i] = min(solutions[i], solutions[i-c] + 1)
        if solutions[amount] == float('inf'):
            return -1
        return solutions[amount]


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1, 2, 5], 11
        expected_output = 3
        output = Solution().coinChange(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [2], 3
        expected_output = -1
        output = Solution().coinChange(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
