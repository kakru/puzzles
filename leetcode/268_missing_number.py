import unittest

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = max(nums)
        sum_ = sum(nums)
        expected_sum = (max_) * (len(nums) + 1)
        if expected_sum % 2 or not expected_sum:  # last number is missing
            return max_ + 1
        else:
            expected_sum /= 2
            result = int(expected_sum - sum_)
            if result in nums:
                return max_ + 1
            else:
                return result

# class Solution:  # best solution from LeetCode  <-- CLEVER, ja probowalem z (min+max)//2 a tutaj len rozwiazuje wszystkie przypadki szczegolne
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         expected_sum = len(nums)*(len(nums)+1)//2
#         actual_sum = sum(nums)
#         return expected_sum - actual_sum
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [3,0,1]
        expected_output = 2
        output = Solution().missingNumber(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [9,6,4,2,3,5,7,0,1]
        expected_output = 8
        output = Solution().missingNumber(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [0]
        expected_output = 1
        output = Solution().missingNumber(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [0,1]
        expected_output = 2
        output = Solution().missingNumber(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = [0,1,2]
        expected_output = 3
        output = Solution().missingNumber(input_)
        self.assertEqual(output, expected_output)

    def test_6(self):
        input_ = [0,1,2,4,5]
        expected_output = 3
        output = Solution().missingNumber(input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)