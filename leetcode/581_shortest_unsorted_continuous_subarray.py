#/usr/bin/env python3
import unittest

class Solution:  # 112 ms (39.80%)
    def findUnsortedSubarray(self, nums: 'List[int]') -> 'int':
        size = len(nums)
        if size < 2: return 0
        i_min = min_v = float("inf")
        i_max = max_v = float("-inf")
        found = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                i_min = min(i_min, i)
                i_max = max(i_max, i+1)
                min_v = min(min_v, nums[i+1])
                max_v = max(max_v, nums[i])
                found = True
        if not found: return 0
        a, b = 0, size-1
        for i in range(size):
            if nums[i] > min_v: break
        a = min(i, i_min)
        for i in range(size):
            if nums[~i] < max_v: break
        b = max(size - i - 1, i_max)
        return b - a + 1



class BasicTest(unittest.TestCase):
    def test_0(self):
        input_ = [1, 1]
        expected_output = 0
        output = Solution().findUnsortedSubarray(input_)
        self.assertEqual(output, expected_output)

    def test_1(self):
        input_ = [2, 6, 4, 8, 10, 9, 15]
        expected_output = 5
        output = Solution().findUnsortedSubarray(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1, 3, 5, 9, 8, 2]
        expected_output = 5
        output = Solution().findUnsortedSubarray(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [1, 1, 1, 1, 1, 2, 1]
        expected_output = 2
        output = Solution().findUnsortedSubarray(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
