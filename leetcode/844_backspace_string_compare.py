#/usr/bin/env python3
import unittest

class Solution:  # 48 ms (24.23%) - O(M+N)
    def backspaceCompare(self, S: 'str', T: 'str') -> 'bool':
        def parse(txt):
            stack = []
            for x in txt:
                if x == "#":
                    if stack: stack.pop()
                else:
                    stack.append(x)
            return stack
        return parse(S) == parse(T)


class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            [("ab#c", "ad#c"), True],
            [("ab##", "c#d#"), True],
            [("a##c", "#a#c"), True],
            [("a#c", "b"), False],
            [("y#fo##f", "y#f#o##f"), True],
        ]:
            self.assertEqual(Solution().backspaceCompare(*test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)  