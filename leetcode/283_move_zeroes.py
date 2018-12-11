#!/usr/bin/env python3
import unittest

class Solution:  # 208ms
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        zeros = nums.count(0)
        if size == zeros: return
        i, done = 0, 0
        # in each step all elements of nums[] for i < done are different than 0
        while i < size - max(done, zeros):
            if nums[i] == 0:
                # find the first non-zero after it
                for j in range(i+1, size):
                    if nums[j]: break
                nums[i], nums[j] = nums[j], nums[i]
            i += 1


# class Solution:  # 44ms, LeetCode best solution
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         writePos = 0
#         for num in nums:
#             if num != 0:
#                 nums[writePos] = num
#                 writePos += 1
#         for i in range(writePos, len(nums)):
#             nums[i] = 0



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [0,1,0,3,12]
        expected_output = [1,3,12,0,0]
        output = input_[:]
        Solution().moveZeroes(output)  # in place
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [0,0,1]
        expected_output = [1,0,0]
        output = input_[:]
        Solution().moveZeroes(output)  # in place
        self.assertEqual(output, expected_output)

    def test_0(self):
        input_ = [0]
        expected_output = [0]
        output = input_[:]
        Solution().moveZeroes(output)  # in place
        self.assertEqual(output, expected_output)

    def test_0s_in_the_end(self):
        input_ = [1,2,3,0,0,0]
        expected_output = [1,2,3,0,0,0]
        output = input_[:]
        Solution().moveZeroes(output)  # in place
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [1,0,1]
        expected_output = [1,1,0]
        output = input_[:]
        Solution().moveZeroes(output)  # in place
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [4,2,4,0,0,3,0,5,1,0]
        expected_output = [4,2,4,3,5,1,0,0,0,0]
        output = input_[:]
        Solution().moveZeroes(output)  # in place
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [1,0]
        expected_output = [1,0]
        output = input_[:]
        Solution().moveZeroes(output)  # in place
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
