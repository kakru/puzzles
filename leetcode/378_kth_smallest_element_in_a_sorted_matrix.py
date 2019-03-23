#/usr/bin/env python3
import unittest
from typing import *

import heapq
class Solution:  # 72 ms (72.82%)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # looking for the k-th smallest element we can store the smallest
        # k elements, and then return the last element from the storage
        # - add first k elements to the storage
        # - iterate over remaining elements and if
        #    * the element is >= than the maximum of the storage - skip it
        #    * the element is < than the maximum - add it to the storage
        #      and get rid of the biggest element in the storage
        #      --> max-heap, in Python heapq provides min-heap, so we store -x
        n = len(matrix)
        storage = []
        for i in range(min(n*n, k)): storage.append(-matrix[i//n][i%n])
        heapq.heapify(storage)
        for i in range(k, n*n):
            element = -matrix[i//n][i%n]
            if element > storage[0]:
                heapq.heappushpop(storage, element)
        return -storage[0]


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[ 1,  5,  9],
                  [10, 11, 13],
                  [12, 13, 15]], 8
        expected_output = 13
        output = Solution().kthSmallest(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)