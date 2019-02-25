#/usr/bin/env python3
import unittest

class Solution:  # 116 ms (100.00%)
    def findJudge(self, N: 'int', trust: 'List[List[int]]') -> 'int':
        if N==1 and len(trust)==0: return 1
        people = set(x[0] for x in trust)
        trusted = set(x[1] for x in trust)
        all_ = set(range(1, N+1))
        result = (all_ - people).intersection(trusted)
        if not result: return -1
        result = result.pop()
        if len(set(x[0] for x in trust if x[1]==result)) == N-1:
            return result
        else:
            return -1


class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            [(2, [[1,2]]), 2],
            [(3, [[1,3],[2,3]]), 3],
            [(3, [[1,3],[2,3],[3,1]]), -1],
            [(3, [[1,2],[2,3]]), -1],
            [(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]), 3],
            [(1, []), 1],
        ]:
            self.assertEqual(Solution().findJudge(*test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)
