#/usr/bin/env python3
import unittest

class Solution(object):  # 44 ms (faster than 96.40%)
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        now1 = max1 = 0
        for n in nums:
            if n:
                now1 += 1
            else:
                max1 = max(max1, now1)
                now1 = 0
        return max(max1, now1)


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,1,0,1,1,1]
        expected_output = 3
        output = Solution().findMaxConsecutiveOnes(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)