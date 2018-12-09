#/usr/bin/env python3
import unittest

class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        sorted_words = sorted(words, key=lambda x: [order.index(i) for i in x])
        return (sorted_words == words)
        


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = ["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
        expected_output = True
        output = Solution().isAlienSorted(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = ["word","world","row"], "worldabcefghijkmnpqstuvxyz"
        expected_output = False
        output = Solution().isAlienSorted(*input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)