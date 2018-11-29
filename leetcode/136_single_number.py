#!/usr/bin/env python3
import unittest

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = nums[0]
        for n in nums[1:]:
            x ^= n
        return x
        


class BasicTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            Solution().singleNumber([2,2,1]),
            1
        )

    def test_2(self):
        self.assertEqual(
            Solution().singleNumber([4,1,2,1,2]),
            4
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)