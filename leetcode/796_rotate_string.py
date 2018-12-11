#/usr/bin/env python3
import unittest

class Solution:  # Brute Force, O(N^2), 36ms
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        sA, sB = len(A), len(B)
        if sA != sB:
            return False
        elif sA == 0:
            return True
        for i in range(sA):
            if A[i:] == B[:-i] and A[:i] == B[-i:]:
                return True
        return False


# class Solution(object):  # LeetCode: clever trick, still O(N^2) [?], in C++ is O(N)
#     def rotateString(self, A, B):
#         return len(A) == len(B) and B in A+A

# Other, better solutions:
# - Rolling Hash - O(N)
# - Knuth-Morris-Pratt - O(N) - string matching (B in A+A) in linear time
# https://leetcode.com/problems/rotate-string/solution/
#
# and:
#    def rotateString(self, A, B):
#        for i, _ in enumerate(A):
#            if A[i+1:] + A[:i+1] == B:
#                return True
#        return False


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "abcde", "cdeab"
        expected_output = True
        output = Solution().rotateString(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "abcde", "abced"
        expected_output = False
        output = Solution().rotateString(*input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = "gcmbf", "fgcmb"
        expected_output = True
        output = Solution().rotateString(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
