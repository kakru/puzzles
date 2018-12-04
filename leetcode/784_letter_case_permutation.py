#/usr/bin/env python3
import unittest

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) == 0: return [""]
        letters = [x.isalpha() for x in S]
        if not any(letters): return [S]
        results = [S]
        while True:
            try:
                i = letters.index(True)
            except ValueError:
                break
            results.extend([
                x[:i] + x[i].upper() + x[i+1:] if x[i].islower() else
                x[:i] + x[i].lower() + x[i+1:] for x in results
            ])
            letters[i] = False
        return results
        


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "a1b2"
        expected_output = ["a1b2", "a1B2", "A1b2", "A1B2"]
        output = Solution().letterCasePermutation(input_)
        self.assertEqual(sorted(output), sorted(expected_output))


if __name__ == '__main__':
    unittest.main(verbosity=2)
