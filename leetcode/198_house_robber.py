#/usr/bin/env python3
import unittest

class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        size = len(nums)
        if size == 0: return 0
        dp = [nums[0]]
        if size > 1:
            dp.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            dp.append(max(nums[i] + dp[i-2], dp[i-1]))
        return dp[-1]


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,3,1]
        expected_output = 4
        output = Solution().rob(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [2,7,9,3,1]
        expected_output = 12
        output = Solution().rob(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
