#/usr/bin/env python3
import unittest

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h_len = len(haystack)
        n_len = len(needle)
        i = 0
        while i <= h_len - n_len:
            if haystack[i:i+n_len] == needle:
                return i
            i += 1
        return -1
    #
    # There is a problem with a step by step solution it's easy to forget about:
    # haystack="mississippi", needle="issippi"
    # mississippi
    #  issippi    --> X
    # mississippi
    #     issippi --> OK
    # the loop index on the haystack cannot go back to 0 !!


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "hello", "ll"
        expected_output = 2
        output = Solution().strStr(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "helo", "ll"
        expected_output = -1
        output = Solution().strStr(*input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = "abc", ""
        expected_output = 0
        output = Solution().strStr(*input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = "abc"*100000, "cab"
        expected_output = 2
        output = Solution().strStr(*input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = "a", "a"
        expected_output = 0
        output = Solution().strStr(*input_)
        self.assertEqual(output, expected_output)

    def test_6(self):
        input_ = "mississippi", "issippi"
        expected_output = 4
        output = Solution().strStr(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)