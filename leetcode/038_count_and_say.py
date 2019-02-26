#/usr/bin/env python3
import unittest

class Solution:  # 48 ms (48.87%)
    def countAndSay(self, n: 'int') -> 'str':
        def count(s):
            res = []
            i = j = 0
            while i+j < len(s):
                v = s[i]
                while i+j < len(s) and s[i+j] == v: j += 1
                res.extend([str(j), v])
                i, j = i+j, 0
            return "".join(res)
        result = "1"
        for _ in range(1, n):
            result = count(result)
        return result


class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            [1, "1"],
            [2, "11"],
            [3, "21"],
            [4, "1211"],
            [5, "111221"],
            [6, "312211"],
            [7, "13112221"],
            [8, "1113213211"],
            [9, "31131211131221"],
            [10, "13211311123113112211"]
        ]:
            self.assertEqual(Solution().countAndSay(test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)