#!/usr/bin/env python3
from typing import *

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # if len(nums) == 0: return 0  # no need to check, the input is a non-empty array
        nums.sort()
        median = nums[len(nums)//2]
        return sum(abs(median-x) for x in nums)