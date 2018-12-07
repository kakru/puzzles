import unittest
from collections import Counter

class Solution:  # 68ms (faster than 64.74%)
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        plate = Counter([x for x in licensePlate.lower() if x.isalpha()])
        min_len = sum(plate.values())
        for word in sorted(words, key=len):
            if len(word) < min_len: continue
            w = Counter(word)
            w.subtract(plate)
            if not any(x < 0 for x in w.values()):
                return word



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "1s3 PSt", ["step", "steps", "stripe", "stepple"]
        expected_output = "steps"
        output = Solution().shortestCompletingWord(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "1s3 456", ["looks", "pest", "stew", "show"]
        expected_output = "pest"
        output = Solution().shortestCompletingWord(*input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)
