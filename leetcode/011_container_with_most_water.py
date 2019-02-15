#/usr/bin/env python3
import unittest

# class Solution:  # Bruteforce
#     def maxArea(self, height: 'List[int]') -> 'int':
#         i, j = 0, len(height)-1
#         maximum = 0
#         for i in range(len(height)-1):
#             for j in range(i+1, len(height)):
#                 maximum = max(maximum, min(height[i], height[j]) * (j-i) )
#         return maximum


class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        i, j = 0, len(height)-1
        maximum = 0
        # finding most left- and most right- container walls
        # while i < len(height)-1 and height[i] == 0: i += 1
        # while j > 0 and height[j] == 0: j += 1
        # reducing container width in steps of 1, choosing the lower wall for each step
        while i < j:
            maximum = max(maximum, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maximum



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,8,6,2,5,4,8,3,7]
        expected_output = 49
        output = Solution().maxArea(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1] + [0]*10000 + [1]
        expected_output = 10001
        output = Solution().maxArea(input_)
        self.assertEqual(output, expected_output)


    # def test_all(self):
    #     for test in [
    #         [("ab", "ba"), True],
    #         [("ab", "ab"), False],
    #         [("aa", "aa"), True],
    #     ]:
    #         self.assertEqual(Solution().solution(*test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)