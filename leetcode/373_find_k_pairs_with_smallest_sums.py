#/usr/bin/env python3
import unittest
from typing import *

import heapq
# class Solution:  # 228 ms (30.00%)
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         results = []
#         for x in nums1:
#             for y in nums2:
#                 if k > 0:
#                     heapq.heappush(results, (-x-y, (x,y)))
#                     k -= 1
#                 else:
#                     heapq.heappushpop(results, (-x-y, (x,y)))
#         return [list(pair[1]) for pair in results]

class Solution:  # 140 ms (37.69%)
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        results = []
        for x in nums1:
            for y in nums2:
                if k > 0:
                    heapq.heappush(results, (-x-y, [x,y]))
                    k -= 1
                else:
                    new_elem = -x-y
                    if results[0][0] < new_elem:
                        heapq.heappushpop(results, (new_elem, [x,y]))
        return [pair[1] for pair in results]



class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            [([1,7,11], [2,4,6], 3), [[1,2],[1,4],[1,6]]],
            [([1,1,2], [1,2,3], 2), [[1,1],[1,1]]],
            [([1,2], [3], 3), [[1,3],[2,3]]],
        ]:
            self.assertEqual(Solution().kSmallestPairs(*test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)