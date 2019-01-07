#/usr/bin/env python3
import unittest

class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        seen = set()
        for n in A:
            if n in seen:
                return n
            else:
                seen.add(n)
        


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,3,3]
        expected_output = 3
        output = Solution().repeatedNTimes(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [2,1,2,5,3,2]
        expected_output = 2
        output = Solution().repeatedNTimes(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [5,1,5,2,5,3,5,4]
        expected_output = 5
        output = Solution().repeatedNTimes(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)