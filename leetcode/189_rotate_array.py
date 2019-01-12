#/usr/bin/env python3
import unittest

"""
- Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
- Could you do it in-place with O(1) extra space?
"""

class Solution:
    def rotate(self, nums, k):  # in-place, O(k*n), O(1) space -- too slow for big input
        nums_len = len(nums)
        k = k % nums_len
        for _ in range(k):
            last = nums[-1]
            for i in range(nums_len-1):
                nums[-i-1] = nums[-i-2]
            nums[0] = last

class Solution:
    def rotate(self, nums, k):  # in-place, O(n), O(k) space
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        k = k % nums_len
        storage = nums[-k:]
        for i in range(nums_len-k):
            nums[-i-1] = nums[-i-1-k]
        for i in range(k):
            nums[i] = storage[i]



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,3,4,5,6,7], 3
        expected_output = [5,6,7,1,2,3,4]
        Solution().rotate(*input_)  # in-place
        self.assertEqual(input_[0], expected_output)

    def test_2(self):
        input_ = [-1,-100,3,99], 2
        expected_output = [3,99,-1,-100]
        Solution().rotate(*input_)  # in-place
        self.assertEqual(input_[0], expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)