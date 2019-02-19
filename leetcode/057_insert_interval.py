#/usr/bin/env python3
import unittest

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        # intervals are initially sorted according to their start times
        s, e = newInterval.start, newInterval.end
        prefix, suffix = [], []
        for i in intervals:
            if i.end < s:
                prefix.append([i.start, i.end])
            elif i.start > e:
                suffix.append([i.start, i.end])
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return prefix + [[s, e]] + suffix


class BasicTest(unittest.TestCase):
    @staticmethod
    def lst2interval(lst):
        return [Interval(x[0], x[1]) for x in lst]
    
    @staticmethod
    def interval2lst(i):
        return [[x.start, x.end] for x in i]

    def test_0(self):
        intervals = [[1,3],[6,9]]
        newInterval = [4,5]
        expected_output = [[1,3],[4,5],[6,9]]
        output = Solution().insert(BasicTest.lst2interval(intervals),
                                   Interval(*newInterval))
        self.assertEqual(output, expected_output)

    def test_1(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]
        expected_output = [[1,5],[6,9]]
        output = Solution().insert(BasicTest.lst2interval(intervals),
                                   Interval(*newInterval))
        self.assertEqual(output, expected_output)

    def test_2(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        expected_output = [[1,2],[3,10],[12,16]]
        output = Solution().insert(BasicTest.lst2interval(intervals),
                                   Interval(*newInterval))
        self.assertEqual(output, expected_output)




if __name__ == '__main__':
    unittest.main(verbosity=2)
