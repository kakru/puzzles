#/usr/bin/env python3
import unittest

class Solution:
    def lengthOfLongestSubstring(self, s):  # 84 ms (faster than 81.93%), mem: 12.5 MB (less than 0.99%)
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size == 0: return 0
        longest_substring_at_pos = [1] * size
        last_position_of_character = {s[0]: 0}
        longest_so_far = 1
        for i, c in enumerate(s[1:], start=1):  # skip the first element, enumerate from 1
            if c in last_position_of_character:
                longest_substring_at_pos[i] = min(longest_substring_at_pos[i-1] + 1,
                                                  i - last_position_of_character[c])
            else:
                longest_substring_at_pos[i] = longest_substring_at_pos[i-1] + 1
            last_position_of_character[c] = i
            longest_so_far = max(longest_so_far, longest_substring_at_pos[i])
        return longest_so_far
# Check the Solution section in LeetCode


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "abcabcbb"
        expected_output = 3  # "abc"
        output = Solution().lengthOfLongestSubstring(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "bbbbb"
        expected_output = 1  # "b"
        output = Solution().lengthOfLongestSubstring(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = "pwwkew"
        expected_output = 3  # "wke"
        output = Solution().lengthOfLongestSubstring(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = " "
        expected_output = 1
        output = Solution().lengthOfLongestSubstring(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = "dvdf"
        expected_output = 3
        output = Solution().lengthOfLongestSubstring(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)