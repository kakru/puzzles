#/usr/bin/env python3
import unittest

class Solution:  # 52 ms (62.02%), recursive with backtracking
    def permute(self, nums):
        result = []
        def p(nums, k=0):
            if k == len(nums):
                result.append(nums[:])
            else:
                for i in range(k, len(nums)):
                    nums[i], nums[k] = nums[k], nums[i]
                    p(nums, k+1)
                    nums[i], nums[k] = nums[k], nums[i]
        p(nums)
        return result
                
        


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,3]
        expected_output = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
        output = Solution().permute(input_)
        self.assertEqual(sorted(output), sorted(expected_output))


if __name__ == '__main__':
    unittest.main(verbosity=2)