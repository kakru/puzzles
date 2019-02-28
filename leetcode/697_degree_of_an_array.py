#/usr/bin/env python3
import unittest

from operator import itemgetter
class Solution:  # 96 ms (59.14%)
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for v in nums: freq[v] = freq.get(v, 0) + 1  # O(n)
        degree = max(freq.values())  # O(n)
        numbers = set([n[0] for n in freq.items() if n[1] == degree])  # O(n)
        mins = {}
        freq = {}
        options = []
        for i, v in enumerate(nums):  # O(k), k <= n
            if v not in numbers: continue
            if v not in mins: mins[v] = i
            freq[v] = freq.get(v, 0) + 1
            if freq[v] == degree:
                options.append(i - mins[v] + 1)
        return min(options)  # O(k), k <= n
            


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1, 2, 2, 3, 1]
        expected_output = 2
        output = Solution().findShortestSubArray(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1,2,2,3,1,4,2]
        expected_output = 6
        output = Solution().findShortestSubArray(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [2,1,1,2,1,3,3,3,1,3,1,3,2]
        expected_output = 7
        output = Solution().findShortestSubArray(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)