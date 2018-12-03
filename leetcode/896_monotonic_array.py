#/usr/bin/env python3
import unittest


class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True
        sign = lambda x: x and (1, -1)[x<0]
        delta = zip(A, A[1:])
        a = sorted([sign(x[1]-x[0]) for x in delta])
        return (max(a) - min(a) <= 1)

# Nicer solution from LeetCode:
class Solution:
    def isIncreasing(self, A):
        return all(a >= b for a,b in zip(A, A[1:]))

    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2: return True
        return self.isIncreasing(A) or self.isIncreasing(A[::-1])




class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,3,4,5]
        expected_output = True
        output = Solution().isMonotonic(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)