#/usr/bin/env python3
import unittest

class Solution:
    def largeGroupPositions(self, S: 'str') -> 'List[List[int]]':
        result = []
        previous, counter = None, 0
        start_pos = 0
        for i, c in enumerate(S):
            if c == previous:
                counter += 1
            else:  # c != previous
                if counter > 2:
                    result.append([start_pos, i-1])
                previous, counter = c, 1
                start_pos = i
        if counter > 2:
            result.append([start_pos, i])
        return result


class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            ["abbxxxxzzy", [[3,6]]],
            ["abc", []],
            ["abcdddeeeeaabbbcd", [[3,5],[6,9],[12,14]]],
            ["aaaa", [[0,3]]],
            ["", []]
        ]:
            self.assertEqual(Solution().largeGroupPositions(test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)