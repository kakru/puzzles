#/usr/bin/env python3
import unittest

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        i, j = 0, 0
        while i < m + n and j < n:
            if nums1[i] <= nums2[j] and i < m+j:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
        del nums1[m+n:]


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,3,0,0,0], 3, [2,5,6], 3
        expected_output = [1,2,2,3,5,6]
        Solution().merge(*input_)
        self.assertEqual(input_[0], expected_output)

    def test_2(self):
        input_ = [1], 1, [], 0
        expected_output = [1]
        Solution().merge(*input_)
        self.assertEqual(input_[0], expected_output)

    def test_3(self):
        input_ = [2,0], 1, [1], 1
        expected_output = [1, 2]
        Solution().merge(*input_)
        self.assertEqual(input_[0], expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)