#!/usr/bin/env python3
import unittest

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        counter = 0
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] == val:  # a number to be skipped
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:  # a number to be kept
                counter += 1
                left += 1
        if nums[left] != val:
            counter += 1
        return counter              
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [3,2,2,3], 3
        expected_output = 2
        output = Solution().removeElement(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [0,1,2,2,3,0,4,2], 2
        expected_output = 5
        output = Solution().removeElement(*input_)
        self.assertEqual(output, expected_output)

    def test_0(self):
        input_ = [], 2
        expected_output = 0
        output = Solution().removeElement(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)