#/usr/bin/env python3
import unittest

class Solution:  # 52 ms (20.37%)
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        size = len(digits)
        if size == 0: return []
        results = []
        def helper(prefix, digit):
            if not digit:
                results.append("".join(prefix))
            else:
                for x in d[digit]:
                    if len(prefix) < size:
                        helper(prefix + [x], digits[len(prefix)])
                    else:
                        helper(prefix + [x], None)
        helper([""], digits[0])
        return results

class Solution:  # 36 ms (68.38%)
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        size = len(digits)
        if size == 0: return []
        results = []
        def helper(prefix, digit):
            for x in d[digit]:
                prefix_length = len(prefix)
                if prefix_length < size:
                    helper(prefix + [x], digits[prefix_length])
                else:
                    results.append("".join(prefix + [x]))
        helper([""], digits[0])
        return results



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "23"
        expected_output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        output = Solution().letterCombinations(input_)
        self.assertEqual(sorted(output), sorted(expected_output))


if __name__ == '__main__':
    unittest.main(verbosity=2)