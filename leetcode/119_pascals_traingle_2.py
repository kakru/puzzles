import unittest


# from math import ceil
# class Solution:  # V1 based - keeping all the results = 36ms
#     def getRow(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         result = [[1],]
#         for i in range(numRows):
#             row = [1] * (i+2)
#             for x in range(1, int(ceil((i+2)/2))):
#                 row[x] = row[~x] = result[-1][x-1] + result[-1][x]
#             result.append(row)
#         return result[-1]

from math import ceil
class Solution:  # v2, only O(k) extra space
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [1]
        for i in range(numRows):
            tmp = [1] * (i+2)
            for x in range(1, int(ceil((i+2)/2))):
                tmp[x] = tmp[~x] = result[x-1] + result[x]
            result = tmp
        return result


# class Solution:  # I like this solution by one of LeetCode users:
#     def getRow(self, numRows):
#         row = [1]
#         for _ in range(rowIndex):
#             row = [x + y for x, y in zip([0]+row, row+[0])]
#         return row



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 0
        expected_output = [1]
        output = Solution().getRow(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 1
        expected_output = [1,1]
        output = Solution().getRow(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 2
        expected_output = [1,2,1]
        output = Solution().getRow(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = 3
        expected_output = [1,3,3,1]
        output = Solution().getRow(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = 4
        expected_output = [1,4,6,4,1]
        output = Solution().getRow(input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)