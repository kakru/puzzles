#!/usr/bin/env python
import unittest

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        words_r = [''.join(reversed(w)) for w in words]
        return ' '.join(words_r)

# class Solution:  # not working
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         ss = list(s)
#         # let's pretend Python doesn't exist
#         p1 = 0
#         p2 = 0
#         while p1 < len(s):
#             print(p1, p2)
#             while ss[p2] and ss[p2] != ' ':
#                 p2 += 1
#             word_start, word_end = p1, p2
#             while p1 < p2:
#                 ss[p1], ss[p2] = ss[p2], ss[p1]
#                 p1 += 1
#                 p2 -= 1
#             if ss[word_end] and ss[word_end] == ' ':
#                 p1 = p2 = word_end + 1
#         return ''.join(ss)


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "Let's take LeetCode contest"
        expected_output = "s'teL ekat edoCteeL tsetnoc"
        output = Solution().reverseWords(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)