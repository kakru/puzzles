import unittest

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        row2 = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        row3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        result = []
        for word in words:
            sword = set(word.lower())
            if len(sword - row1) == 0 or len(sword - row2) == 0 or len(sword - row3) == 0:
                result.append(word)
        return result           
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = ["Hello", "Alaska", "Dad", "Peace"]
        expected_output = ["Alaska", "Dad"]
        output = Solution().findWords(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)