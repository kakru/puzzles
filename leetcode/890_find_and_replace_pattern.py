#/usr/bin/env python3
import unittest

"""
You have a list of words and a pattern, and you want to know which words in words matches the pattern.
A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)
Return a list of the words in words that match the given pattern. 
You may return the answer in any order.
"""

from collections import Counter
# class Solution:
#     def findAndReplacePattern(self, words, pattern):
#         """
#         :type words: List[str]
#         :type pattern: str
#         :rtype: List[str]
#         """
#         results = []
#         c_pattern = Counter(pattern)
#         for word in words:
#             if len(word) != len(pattern):
#                 continue
#             original_word = word[:]
#             c_word = Counter(word)
#             if sorted(c_word.values()) != sorted(c_pattern.values()):
#                 continue
#             w = word[:]
#             p = pattern[:]
#             for i, (a, b) in enumerate(zip(c_word.keys(), c_pattern.keys())):
#                 w = w.replace(a, chr(i))
#                 p = p.replace(b, chr(i))
#             if w == p:
#                 results.append(original_word)
#         return results


class Solution:
    def findAndReplacePattern(self, words, p):
        def N(w):
            norm = {}
            return [norm.setdefault(c, len(norm)) for c in w]
        return [w for w in words if N(w) == N(p)]



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = ["abc","deq","mee","aqq","dkd","ccc"], "abb"
        expected_output = ["mee","aqq"]
        output = Solution().findAndReplacePattern(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = ["abc","cba","xyx","yxx","yyx"], "abc"
        expected_output = ["abc","cba"]
        output = Solution().findAndReplacePattern(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
