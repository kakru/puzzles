#/usr/bin/env python3
import unittest

class Solution:  # naive solution, O(n), with space complexity O(3n) = O(n)
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_numbers = []
        odd_numbers = []
        for n in A:
            if n%2:
                even_numbers.append(n)
            else:
                odd_numbers.append(n)
        for i in range(0, len(A), 2):
            A[i] = odd_numbers[i//2]
            A[i+1] = even_numbers[i//2]
        return A


# BETTER SOLUTION - in-place:
class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [4,2,5,7]
        expected_output = [4,5,2,7]
        output = Solution().sortArrayByParityII(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)