#/usr/bin/env python3
import unittest

# # working solution
# class Solution:
#     def findLengthOfLCIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         i, size = 1, len(nums)
#         if size < 2: return size
#         lcis = 0
#         counter = 0
#         while i < size:
#             if nums[i] <= nums[i-1]:
#                 lcis = max(lcis, counter)
#                 counter = 0
#             else:
#                 counter += 1
#             i += 1
#         return max(lcis+1, counter+1)

from itertools import groupby
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lcis = 0
        for k, g in groupby(a < b for a,b in zip(nums, nums[1:])):
            if k: lcis = max(lcis, len(list(g)))
        return lcis+1


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,3,5,4,7]
        expected_output = 3
        output = Solution().findLengthOfLCIS(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1,2,3,4,5]
        expected_output = 5
        output = Solution().findLengthOfLCIS(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [1,1,1]
        expected_output = 1
        output = Solution().findLengthOfLCIS(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)