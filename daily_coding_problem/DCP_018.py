#/usr/bin/env python3
import unittest

from collections import deque

class Solution:
    def solution(self, A, k):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = deque(A[:k-1])
        R = []
        for i in range(len(A)-k+1):
            B.append(A[i+k-1])
            R.append(max(B))
            B.popleft()
        return R
        
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [10,5,2,7,8,7], 3
        expected_output = [10,7,8,8]
        output = Solution().solution(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [10,5,2,7,8,7], 1
        expected_output = [10,5,2,7,8,7]
        output = Solution().solution(*input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [10,5,2,7,8,7], 6
        expected_output = [10]
        output = Solution().solution(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)