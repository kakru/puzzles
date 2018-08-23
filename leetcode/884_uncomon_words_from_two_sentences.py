import unittest

from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        words_A = Counter(A.split())
        words_B = Counter(B.split())
        words = sum((words_A, words_B), Counter())
        # instead I could have used:
        # words = Counter((A + " " + B).split())
        return [k for k, v in words.items() if v==1]
        # return [w for w in words if words[w] == 1]

        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_A = "this apple is sweet"
        input_B = "this apple is sour"
        expected_output = ["sweet","sour"]
        output = Solution().uncommonFromSentences(input_A, input_B)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_A = "apple apple"
        input_B = "banana"
        expected_output = ["banana"]
        output = Solution().uncommonFromSentences(input_A, input_B)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)