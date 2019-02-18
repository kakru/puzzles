#/usr/bin/env python3
import unittest

class Solution:
    def reverseVowels(self, s: 'str') -> 'str':
        size = len(s)
        if size < 2: return s
        vowels = set(['a', 'e', 'i', 'o', 'u',
                      'A', 'E', 'I', 'O', 'U'])
        s = list(s)  # immutable strings in Python, using list of characters
        i, j = 0, size - 1
        while i < j:
            while i < j and s[i] not in vowels: i += 1
            while i < j and s[j] not in vowels: j -= 1
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "hello"
        expected_output = "holle"
        output = Solution().reverseVowels(input_)
        self.assertEqual(output, expected_output)


    # def test_all(self):
    #     for test in [
    #         [("ab", "ba"), True],
    #         [("ab", "ab"), False],
    #         [("aa", "aa"), True],
    #     ]:
    #         self.assertEqual(Solution().reverseVowels(*test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)