#/usr/bin/env python3
import unittest

# class Solution:  # Bruteforce... 156 ms (71.07%), 14.3 MB (74.27%)
#     def sortedSquares(self, A: 'List[int]') -> 'List[int]':
#         return sorted([x**2 for x in A])

class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        size = len(A)
        if size == 0:
            return []
        elif size == 1:
            return [A[0]*A[0]]
        ans = []
        # find where in A the non-negative numbers start
        # j = 0
        # while j < size - 1 and A[j] < 0: j += 1
        i, j = 0, size - 1
        while i < j:
            mid = (j + i) // 2
            if A[mid] < 0:
                i = mid + 1
            else:
                j = mid
        # use two pointers, while "i" will be decreasing until 0
        # "j" will be increasing until "size-1"
        i = j-1
        while i >= 0 or j < size:
            if j < size and A[i] * A[i] >= A[j] * A[j]:
                ans.append(A[j]*A[j])
                j += 1
            else:
                ans.append(A[i]*A[i])
                i -= 1
        return ans




class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [-4,-1,0,3,10]
        expected_output = [0,1,9,16,100]
        output = Solution().sortedSquares(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [-7,-3,2,3,11]
        expected_output = [4,9,9,49,121]
        output = Solution().sortedSquares(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [-1,1]
        expected_output = [1,1]
        output = Solution().sortedSquares(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)