#/usr/bin/env python3
import unittest

"""Given a string of words delimited by spaces, reverse the words in string.
For example, given "hello world here", return "here world hello"
"""

class Solution:
    def solution(self, s):
        # not in-place (stings):
        # return ' '.join(s.split(' ')[::-1])
        #
        # in place (lists):
        size = len(s)
        i = 0
        while i < size:
            j1 = j2 = i
            while (j2 < size) and (s[j2] != ' '): j2 += 1
            for k in range((j2-j1)//2):
                s[j1+k], s[j2-k-1] = s[j2-k-1], s[j1+k]
            i = j2 + 1
        for i in range(size//2):
            s[i], s[-i-1] = s[-i-1], s[i]
        
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "hello world here"
        expected_output = "here world hello"
        input_ = list(input_)
        expected_output = list(expected_output)
        Solution().solution(input_)  # in-place
        self.assertEqual(input_, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
