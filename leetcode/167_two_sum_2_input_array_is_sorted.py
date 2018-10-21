import unittest

# Caution: Your returned answers (both index1 and index2) are not zero-based.

# Compare with 1.
# let's try to solve it with O(n) in time, and O(1) in storage



class Solution:
    def twoSum(self, numbers, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s > target:
                right -= 1
            else:
                left += 1
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [2, 7, 11, 15], 9
        expected_output = [1, 2]
        output = Solution().twoSum(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [2, 3, 4], 6
        expected_output = [1, 3]
        output = Solution().twoSum(*input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [3, 3], 6
        expected_output = [1, 2]
        output = Solution().twoSum(*input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [5,25,75], 100
        expected_output = [2, 3]
        output = Solution().twoSum(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)