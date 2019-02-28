#!/usr/bin/env python3

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(x):
    return x>3

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, hi = 0, n
        while low < hi:
            mid = (low+hi) // 2
            is_bad = isBadVersion(mid)
            if is_bad:
                hi = mid
            else:
                low = mid + 1
        return low


print(Solution().firstBadVersion(10))