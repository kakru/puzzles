#/usr/bin/env python3
import unittest


class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): return False
        # looking for characters that differ
        diff = []
        for i in range(len(A)):
            if A[i] != B[i]: diff.append(i)
        size = len(diff)
        if size == 2:
            return A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]
        elif size == 0:
            return len(set(A)) < len(A)
        return False



class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            [("ab", "ba"), True],
            [("ab", "ab"), False],
            [("aa", "aa"), True],
            [("aaaaaaabc", "aaaaaaacb"), True],
            [("", "aa"), False],
            [("abcaa", "abcbb"), False],
            [("abc", "acd"), False],
        ]:
            self.assertEqual(Solution().buddyStrings(*test[0]), test[1])
        


if __name__ == '__main__':
    unittest.main(verbosity=2)
