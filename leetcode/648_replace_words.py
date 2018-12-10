#/usr/bin/env python3
import unittest

class Solution:  # 480ms, best solution is < 60ms
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split(" ")
        roots = sorted(dict)
        for i in range(len(words)):
            common = [words[i].startswith(x) for x in roots]
            if True in common:
                words[i] = roots[common.index(True)]
        return " ".join(words)
        


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = ["cat", "bat", "rat"], "the cattle was rattled by the battery"
        expected_output = "the cat was rat by the bat"
        output = Solution().replaceWords(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
