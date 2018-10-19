import unittest
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # return all(ransomNote.count(char) <= magazine.count(char) for char in set(ransomNote))
        letters_note = Counter(ransomNote)
        letters_magazine = Counter(magazine)
        for letter in letters_note.keys():
            if (letter not in letters_magazine
                    or letters_magazine[letter] < letters_note[letter]):
                return False
        return True
        
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = ("a", "b")
        expected_output = False
        output = Solution().canConstruct(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = ("aa", "ab")
        expected_output = False
        output = Solution().canConstruct(*input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = ("aa", "aab")
        expected_output = True
        output = Solution().canConstruct(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)