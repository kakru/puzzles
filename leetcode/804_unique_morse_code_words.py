import unittest

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        words_in_morse = [
            ''.join([morse[ord(letter)-97] for letter in word]) for word in words
        ]
        unique_transformations = set(words_in_morse)
        return len(unique_transformations)
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = ["gin", "zen", "gig", "msg"]
        expected_output = 2
        output = Solution().uniqueMorseRepresentations(input_)
        self.assertEqual(output, expected_output)
        

if __name__ == '__main__':
    unittest.main(verbosity=2)