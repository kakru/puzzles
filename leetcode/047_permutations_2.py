#/usr/bin/env python3
import unittest
from typing import *

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        def p(nums, k=0):
            if k == len(nums):
                result.add(tuple(nums))
            else:
                for i in range(k, len(nums)):
                    nums[i], nums[k] = nums[k], nums[i]
                    p(nums, k+1)
                    nums[i], nums[k] = nums[k], nums[i]
        p(nums)
        return [list(x) for x in result]


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,1,2]
        expected_output = [[1,1,2], [1,2,1], [2,1,1]]
        output = Solution().permuteUnique(input_)
        self.assertEqual(sorted(output), sorted(expected_output))


if __name__ == '__main__':
    unittest.main(verbosity=2)