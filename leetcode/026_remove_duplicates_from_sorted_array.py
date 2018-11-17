#/usr/bin/env python3
import unittest

# class Solution:  # Best solution, but not mine
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 0:
#             return 0
#         j = 0
#         num = len(nums)
#         for i in range(num):
#             if nums[j] != nums[i]:
#                 nums[j+1] = nums[i]
#                 j += 1
#         return j + 1


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return 1
        # find first repeated element
        p1 = 1
        while p1 < length:
            if nums[p1] == nums[p1-1]:
                break
            p1 += 1
        else:  # no repeated element in the given array
            return length
        curr_max = nums[p1]
        # find first element bigger than curr_max
        p2 = p1
        while p2 < length:
            if nums[p2] > curr_max:
                break
            p2 += 1
        else:  # no element bigger
            return p1
        ### START LOOPING
        while True:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            curr_max = nums[p1]
            p1 += 1
            while p2 < length:
                if nums[p2] > curr_max:
                    break
                p2 += 1
            else:  # no more elements bigger than curr_max
                break
        return p1


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,1,2]
        expected_output = 2
        output = Solution().removeDuplicates(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1,1,2,2,3]
        expected_output = 3
        output = Solution().removeDuplicates(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [1,1,1,1,3]
        expected_output = 2
        output = Solution().removeDuplicates(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [0,0,1,1,1,2,2,3,3,4]
        expected_output = 5
        output = Solution().removeDuplicates(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = [1,2]
        expected_output = 2
        output = Solution().removeDuplicates(input_)
        self.assertEqual(output, expected_output)

    def test_6(self):
        input_ = [1,2,2]
        expected_output = 2
        output = Solution().removeDuplicates(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)