#/usr/bin/env python3
import unittest

"""A string S of lowercase letters is given. We want to partition
this string into as many parts as possible so that each letter appears
in at most one part, and return a list of integers representing the
size of these parts."""


class Solution:  # 84 ms (19.74%), 12.5 MB (100.00%)
    def partitionLabels(self, S: 'str') -> 'List[int]':
        # S will consist of lowercase letters ('a' to 'z') only
        # so this can be improved by using a list (array) instead of {}
        start, end = {}, {}
        for i, x in enumerate(S):
            if x in start:  # <==> x in start and x in end
                start[x] = min(start[x], i)
                end[x] = max(end[x], i)
            else:
                start[x], end[x] = i, i
        intervals = [[start[x], end[x]] for x in start.keys()]
        if len(intervals) == 1: return [len(intervals)]
        # let's merge patially overlapping intervals
        s, e = intervals[0]
        merged = []
        for i in intervals[1:]:
            if s <= i[0] < e:
                e = max(e, i[1])
            else:
                merged.append([s, e])
                s, e = i
        merged.append([s, e])
        # interval lengths
        return [x[1]-x[0]+1 for x in merged]


## Leetcode solution
# class Solution(object):
#     def partitionLabels(self, S):
#         last = {c: i for i, c in enumerate(S)}
#         j = anchor = 0
#         ans = []
#         for i, c in enumerate(S):
#             j = max(j, last[c])
#             if i == j:
#                 ans.append(i - anchor + 1)
#                 anchor = i + 1
#         return ans


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "ababcbacadefegdehijhklij"
        expected_output = [9,7,8]
        output = Solution().partitionLabels(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "ababcbacah"
        expected_output = [9,1]
        output = Solution().partitionLabels(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)