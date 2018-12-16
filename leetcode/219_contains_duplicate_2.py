#/usr/bin/env python3
import unittest

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i, n in enumerate(nums):
            # if n in seen and abs(seen[n] - i) <= k:
            if n in seen and i - seen[n] <= k:
                return True
            else:
                seen[n] = i
        return False


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,3,1], 3
        expected_output = True
        output = Solution().containsNearbyDuplicate(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1,0,1,1], 1
        expected_output = True
        output = Solution().containsNearbyDuplicate(*input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [1,2,3,1,2,3], 2
        expected_output = False
        output = Solution().containsNearbyDuplicate(*input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [1,2,3,1,2,3,2], 2
        expected_output = True
        output = Solution().containsNearbyDuplicate(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
