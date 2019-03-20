#/usr/bin/env python3
import unittest

# class Solution:  # 40 ms and O(n) extra space needed
#     def firstMissingPositive(self, nums: 'List[int]') -> 'int':
#         if not nums: return 1
#         min_ = min(nums)
#         max_ = max(nums)
#         if min_ > 1: return 1
#         A = [0] * (len(nums) + 1)
#         A[0] = 1
#         for x in nums:
#             if x >= 0 and x <= len(nums):
#                 A[x] = 1
#         if 0 not in A:
#             return max_ + 1
#         ret = A.index(0)
#         return ret

class Solution:  # 40 ms (63.12%) and O(1) extra space
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        if not nums: return 1
        size = len(nums)
        i = 0
        while True:
            if nums[i] <= 0 or nums[i] >= size or nums[i] == i+1:
                i += 1 
            else:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                if (i >= 0 and i < size
                    and nums[i] >= 1 and nums[i]-1 < size
                    and nums[nums[i]-1] == nums[i]):
                        i += 1
            if i >= size:
                break
        for i in range(size):
            if nums[i] != i+1: return i + 1
        return size + 1


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,0]
        expected_output = 3
        output = Solution().firstMissingPositive(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [3,4,-1,1]
        expected_output = 2
        output = Solution().firstMissingPositive(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [7,8,9,11,12]
        expected_output = 1
        output = Solution().firstMissingPositive(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [2,-1,4,1,5]
        expected_output = 3
        output = Solution().firstMissingPositive(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = [1,1]
        expected_output = 2
        output = Solution().firstMissingPositive(input_)
        self.assertEqual(output, expected_output)

    def test_6(self):
        input_ = [1]
        expected_output = 2
        output = Solution().firstMissingPositive(input_)
        self.assertEqual(output, expected_output)

    def test_7(self):
        input_ = [-10,-3,-100,-1000,-239,1]
        expected_output = 2
        output = Solution().firstMissingPositive(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)