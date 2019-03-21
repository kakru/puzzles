#/usr/bin/env python3
import unittest

# class Solution:  # 228 ms (18.16%)
#     def findDuplicates(self, nums: 'List[int]') -> 'List[int]':
#         size = len(nums)
#         if size < 2: return []
#         i, results = 0, set()
#         while i < size:
#             if nums[i] < 0 or nums[i] == i + 1:
#                 i += 1
#             else:
#                 if nums[nums[i]-1] != -nums[i]:
#                     nums[nums[i]-1], nums[i] = -(nums[i]), nums[nums[i]-1]
#                 else:
#                     results.add(nums[i])
#                     i += 1
#         return list(results)

class Solution:  # 220 ms (21.65%)
    def findDuplicates(self, nums: 'List[int]') -> 'List[int]':
        size = len(nums)
        if size < 2: return []
        i, results = 0, []
        while i < size:
            while i != nums[i]-1 and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            i += 1
        for i in range(size):
            if i != nums[i]-1: results.append(nums[i])
        return results


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [4,3,2,7,8,2,3,1]
        expected_output = [2,3]
        output = Solution().findDuplicates(input_)
        self.assertEqual(sorted(output), sorted(expected_output))

    def test_2(self):
        input_ = [1,1]
        expected_output = [1]
        output = Solution().findDuplicates(input_)
        self.assertEqual(sorted(output), sorted(expected_output))

    def test_3(self):
        input_ = [2,2]
        expected_output = [2]
        output = Solution().findDuplicates(input_)
        self.assertEqual(sorted(output), sorted(expected_output))


if __name__ == '__main__':
    unittest.main(verbosity=2)
