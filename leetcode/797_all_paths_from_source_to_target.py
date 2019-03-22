#/usr/bin/env python3
import unittest
from typing import *

class Solution:  # 152 ms (61.23%)
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        results = []
        destination = len(graph) - 1
        def dfs(results, path):
            node = path[-1]
            if node == destination:
                results.append(path[:])
            else:
                for nxt in graph[node]:
                    path.append(nxt)
                    dfs(results, path)
                    path.pop()
        dfs(results, [0])
        return results
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[1,2], [3], [3], []]
        expected_output = [[0,1,3],[0,2,3]]
        output = Solution().allPathsSourceTarget(input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)