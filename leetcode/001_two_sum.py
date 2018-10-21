import unittest

# Compare with 167.

# the array is not sorted, and we are asked for indeces, not the values
# on the other hand, we know that there is only one solution (? - not sure, cause:
# [3,3],6 test case can give [0, 1] and [1, 0] answers
# anyway, let's assume it's like that

# we want one pass on the list to achieve O(1) in time

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        missing = {}
        for i, n in enumerate(nums):
            if n in missing:
                return [missing[n], i]
            else:
                missing[target-n] = i
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [2, 7, 11, 15], 9
        expected_output = [0, 1]
        output = Solution().twoSum(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [3, 2, 4], 6
        expected_output = [1, 2]
        output = Solution().twoSum(*input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [3, 3], 6
        expected_output = [0, 1]
        output = Solution().twoSum(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)