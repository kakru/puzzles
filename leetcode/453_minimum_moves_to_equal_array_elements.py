#!/usr/bin/env python3
from typing import *

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #return sum(nums) - (len(nums) * min(nums))
        sum_, len_, min_ = 0, len(nums), float("inf")
        for number in nums:
            sum_ += number
            if number < min_: min_ = number
        return sum_ - len_ * min_