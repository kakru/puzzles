#/usr/bin/env python3
import unittest

from heapq import heapify, heappop
from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck):  # 68 ms - accepted solution
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        heapify(deck)
        available = deque([i for i in range(len(deck))])
        ans = [None for i in range(len(deck))]
        while available:
            try:
                pos = available.popleft()
                ans[pos] = heappop(deck)
                available.append(available.popleft())
            except IndexError:
                return ans


# class Solution:  # TODO: skip first half of deck elements
#     def deckRevealedIncreasing(self, deck):
#         """
#         :type deck: List[int]
#         :rtype: List[int]
#         """
#         heapify(deck)
#         available = deque([i for i in range(len(deck)) if i%2 == 1])
#         # available = deque([i for i in range(len(deck))])
#         # first half of the numbers are straight forward
#         ans = [heappop(deck) if i%2 == 0 else None for i in range(len(deck))]
#         # ans = [None for i in range(len(deck))]
#         while available:
#             try:
#                 pos = available.popleft()
#                 ans[pos] = heappop(deck)
#                 pos = available.popleft()
#                 available.append(pos)
#             except IndexError:
#                 return ans


class BasicTest(unittest.TestCase):
    def test_0(self):
        input_ = [1,2,3,4,5,6,7,8,9,10,11]
        expected_output = [1,7,2,11,3,8,4,10,5,9,6]
        output = Solution().deckRevealedIncreasing(input_)
        self.assertEqual(output, expected_output)

    def test_1(self):
        input_ = [17,13,11,2,3,5,7]
        expected_output = [2,13,3,11,5,17,7]
        output = Solution().deckRevealedIncreasing(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
