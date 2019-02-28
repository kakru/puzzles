#/usr/bin/env python3
import unittest

class Solution:
    def solution(self, A):
        pass


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,3,4,5]
        expected_output = 2
        output = Solution().solution(input_)
        self.assertEqual(output, expected_output)


    def test_all(self):
        for test in [
            [("ab", "ba"), True],
            [("ab", "ab"), False],
            [("aa", "aa"), True],
        ]:
            self.assertEqual(Solution().solution(*test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)