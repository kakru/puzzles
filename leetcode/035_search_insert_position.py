#!/usr/bin/env python3
import unittest

"""
Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""

class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        size = len(nums)
        left, right = 0, size-1
        while left <= right:
            middle = (left+right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:  # nums[middle] == target
                return middle
        return left



class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            [([1,3,5,6], 5), 2],
            [([1,3,5,6], 2), 1],
            [([1,3,5,6], 7), 4],
            [([1,3,5,6], 0), 0],
        ]:
            self.assertEqual(Solution().searchInsert(*test[0]), test[1])


unittest.main(verbosity=2)

