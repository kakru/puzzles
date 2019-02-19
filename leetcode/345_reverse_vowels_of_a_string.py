#/usr/bin/env python3
import unittest

class Solution:  # 60 ms (94,78%), 13.3 MB (100.00%)
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
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)


## With Regex (LeetCode)
# class Solution:
#     def reverseVowels(self, s):
#         vowels = re.findall('(?i)[aeiou]', s)
#         return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "hello"
        expected_output = "holle"
        output = Solution().reverseVowels(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "hhhhssss"
        expected_output = "hhhhssss"
        output = Solution().reverseVowels(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)