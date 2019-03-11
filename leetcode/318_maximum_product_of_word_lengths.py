#/usr/bin/env python3
import unittest

from operator import itemgetter
class Solution:  # 436 ms (59.45%)
    def maxProduct(self, words: 'List[str]') -> 'int':
        def bitmap(word):
            b = 0
            for letter in word: b |= (1 << ord(letter)-97)
            return b
        size = len(words)
        bitmaps = [bitmap(w) for w in words]
        longest_words = sorted(zip((len(w) for w in words), bitmaps))
        best = 0
        for i in range(size):
            for j in range(i, size):
                if not (longest_words[i][1] & longest_words[j][1]):
                    best = max(best, longest_words[i][0] * longest_words[j][0])
        return best


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = ["abcw","baz","foo","bar","xtfn","abcdef"]
        expected_output = 16  # The two words can be "abcw", "xtfn".
        output = Solution().maxProduct(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = ["a","ab","abc","d","cd","bcd","abcd"]
        expected_output = 4  # The two words can be "ab", "cd".
        output = Solution().maxProduct(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = ["a","aa","aaa","aaaa"]
        expected_output = 0
        output = Solution().maxProduct(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)