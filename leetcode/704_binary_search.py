#!/usr/bin/env python3

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        if right == 0: return -1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:  # nums[mid] == target
                return mid
        return -1
