#!/usr/bin/env python3

from collections import Counter
class Solution:
    def commonChars(self, A):
        if not A: return []
        B = [Counter(a) for a in A]
        result = Counter(B[0])
        for i in range(1, len(B)):
            result &= B[i]
        return list(result.elements())

print(Solution().commonChars(["bella", "lable", "roller"]))
