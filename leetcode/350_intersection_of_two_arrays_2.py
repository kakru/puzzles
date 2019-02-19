#/usr/bin/env python3
import unittest

from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        # return (c1 & c2).elements()  # itertools.chain - Not implemented in LeetCode Parser
        res = []
        for x in [[e] * i for e, i in (c1 & c2).most_common()]:
            res.extend(x)
        return res


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,2,1], [2,2]
        expected_output = [2,2]
        output = Solution().intersect(*input_)
        self.assertEqual(sorted(output), sorted(expected_output))

    def test_2(self):
        input_ = [4,9,5], [9,4,9,8,4]
        expected_output = [4,9]
        output = Solution().intersect(*input_)
        self.assertEqual(sorted(output), sorted(expected_output))


if __name__ == '__main__':
    unittest.main(verbosity=2)