#/usr/bin/env python3
import unittest

class Solution:
    # # by rule: N=1bln --> 284 sek.
    # def prisonAfterNDays(self, cells, N):
    #     c = [bool(x) for x in cells]
    #     # print([int(x) for x in c])
    #     for i in range(N):
    #         c = [False, c[0]==c[2], c[1]==c[3], c[2]==c[4], c[3]==c[5], c[4]==c[6], c[5]==c[7], False]
    #         # print([int(x) for x in c])
    #     return [int(x) for x in c]

    # # changed to tuples to try caching the reasults (8 cells --> max. 264 options anyway)
    # cache for the second provided example end up being of size 15 (14 repeating combinations + the starting one)
    def prisonAfterNDays(self, cells, N):
        c = tuple(bool(x) for x in cells)
        for _ in range(N%14 or 14):
            c = (False, c[0]==c[2], c[1]==c[3], c[2]==c[4],
                 c[3]==c[5], c[4]==c[6], c[5]==c[7], False)
        return [int(x) for x in c]




class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [0,1,0,1,1,0,0,1], 7
        expected_output = [0,0,1,1,0,0,0,0]
        output = Solution().prisonAfterNDays(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1,0,0,1,0,0,1,0], 1000000000
        expected_output = [0,0,1,1,1,1,1,0]
        output = Solution().prisonAfterNDays(*input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [1,0,0,1,0,0,0,1], 826
        expected_output = [0,1,1,0,1,1,1,0]
        output = Solution().prisonAfterNDays(*input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [1,0,1,0,0,0,1,0], 788566492
        expected_output = [0,0,0,0,1,0,0,0]
        output = Solution().prisonAfterNDays(*input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)
