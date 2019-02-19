#/usr/bin/env python3
import unittest

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    
class Solution:  # 60 ms (84.15%), 15.3 MB (100.00%)
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if not intervals: return []
        result = []
        intervals.sort(key=lambda x: (x.start, -x.end))
        start, end = intervals[0].start, intervals[0].end
        i = 0
        while i < len(intervals):
            if intervals[i].start <= end:
                end = max(end, intervals[i].end)
                i += 1
            else:
                result.append([start, end])
                while i < len(intervals) and intervals[i].start <= end:
                    i += 1
                else:
                    start, end = intervals[i].start, intervals[i].end
        if not result or result[-1] != [start, end]:
            result.append([start, end])
        return result


class BasicTest(unittest.TestCase):
    @staticmethod
    def lst2interval(lst):
        return [Interval(x[0], x[1]) for x in lst]
    
    @staticmethod
    def interval2lst(i):
        return [[x.start, x.end] for x in i]
        
    def test_1(self):
        input_ = [[1,3],[2,6],[8,10],[15,18]]
        expected_output = [[1,6],[8,10],[15,18]]
        output = Solution().merge(BasicTest.lst2interval(input_))
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [[1,4],[4,5]]
        expected_output = [[1,5]]
        output = Solution().merge(BasicTest.lst2interval(input_))
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [[1,4],[1,5]]
        expected_output = [[1,5]]
        output = Solution().merge(BasicTest.lst2interval(input_))
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)
