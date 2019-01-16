#/usr/bin/env python3
import unittest

"""Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K."""

# class Solution:
#     def subarraysDivByK(self, A, K):
#         """
#         :type A: List[int]
#         :type K: int
#         :rtype: int
#         """
#         size = len(A)
#         counter = 0
#         for left in range(size+1):
#             for right in range(left, size+1):
#                 if left != right and sum(A[left:right]) % K == 0:
#                     counter += 1
#         return counter


from collections import defaultdict
class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        mods = defaultdict(int)
        mods[0] = 1
        count = 0
        total = 0
        for a in A:
            total += a
            m = total % K
            if m in mods: count += mods[m]
            mods[m] += 1
        return count



class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            [([4,5,0,-2,-3,1], 5), 7],
            [([5], 9), 0],
            [([0]*10000, 1000), 50005000],  # Time Limit Exceeded with a traditional approach
        ]:
            self.assertEqual(Solution().subarraysDivByK(*test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)
