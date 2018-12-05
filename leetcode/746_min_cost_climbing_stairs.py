#/usr/bin/env python3
import unittest
from functools import lru_cache

## Recursive solution (84ms)
# class Solution:
#     @lru_cache(maxsize=None)
#     def startingWith(self, i):
#         if i >= self.cost_len: return 0
#         return self.cost[i] + min(
#             self.startingWith(i+1),
#             self.startingWith(i+2))

#     def minCostClimbingStairs(self, cost):
#         """
#         :type cost: List[int]
#         :rtype: int
#         """
#         self.cost = cost
#         self.cost_len = len(cost)
#         return min(self.startingWith(0), self.startingWith(1))
        

## Iterative solution (44ms)
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = f2 = 0
        for i in reversed(cost):
            f1, f2 = i + min(f1, f2), f1
        return min(f1, f2)


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [10, 15, 20]
        expected_output = 15
        output = Solution().minCostClimbingStairs(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        expected_output = 6
        output = Solution().minCostClimbingStairs(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
