#!/usr/bin/env python3

class Solution:  # 84 ms (41.21%)
    def pivotIndex(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return -1
        elif size == 1:
            return 1
        total = sum(nums)
        add = 0
        for i, v in enumerate(nums):
            if total - add == add + v:
                return i
            add += v
        return -1
