#/usr/bin/env python3
import unittest

class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return len(set(
            tuple(sorted(s[0::2]) + sorted(s[1::2])) for s in A))
        ## or:
        # smallest_special_equivalents = set()
        # for s in A:
        #     smallest_special_equivalents.add(
        #         tuple(sorted(s[0::2]) + sorted(s[1::2])))
        # return len(smallest_special_equivalents)        


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = ["a","b","c","a","c","c"]
        expected_output = 3
        output = Solution().numSpecialEquivGroups(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = ["aa","bb","ab","ba"]
        expected_output = 4
        output = Solution().numSpecialEquivGroups(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = ["abc","acb","bac","bca","cab","cba"]
        expected_output = 3
        output = Solution().numSpecialEquivGroups(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = ["abcd","cdab","adcb","cbad"]
        expected_output = 1
        output = Solution().numSpecialEquivGroups(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
