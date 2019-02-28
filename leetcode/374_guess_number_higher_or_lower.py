#!/usr/bin/env python3

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):  # 16 ms (100.00%)
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, hi = 0, n+1
        while low < hi:
            mid = (low+hi) // 2
            result = guess(mid)
            if result == 1:
                low = mid + 1
            elif result == -1:
                hi = mid - 1
            else:  # result == 0
                return mid
        return low
        
