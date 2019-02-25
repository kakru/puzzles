#/usr/bin/env python3
import unittest

class Solution:  # 52 ms (32.69%)
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if n == 0: return []
        result = []
        def is_correct(p):
            s = []
            for x in p:
                if x == "(":
                    s.append("(")
                else:  # x == ")"
                    if not s: return False
                    s.pop() == "("
            return len(s) == 0
        def helper(stack, open_, close_):
            if open_ == close_ == n:
                candidate = "".join(stack)
                if is_correct(candidate):
                    result.append(candidate)
            else:
                if open_ < n:
                    # try opening a new one
                    stack.append("(")
                    helper(stack, open_ + 1, close_)
                    stack.pop()
                if close_ < open_:
                    # try closing
                    stack.append(")")
                    helper(stack, open_, close_ + 1)
                    stack.pop()
        helper([], 0, 0)
        return result


class Solution:  # 48 ms (40.10%)
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if n == 0: return []
        result = []
        def helper(stack, open_, close_):
            if open_ == close_ == n:
                result.append("".join(stack))
            else:
                if open_ < n:
                    # try opening a new one
                    stack.append("(")
                    helper(stack, open_ + 1, close_)
                    stack.pop()
                if close_ < open_:
                    # try closing
                    stack.append(")")
                    helper(stack, open_, close_ + 1)
                    stack.pop()
        helper([], 0, 0)
        return result

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 1
        expected_output = [
            "()",
        ]
        output = Solution().generateParenthesis(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 3
        expected_output = [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ]
        output = Solution().generateParenthesis(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)