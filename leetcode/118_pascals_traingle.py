import unittest


from math import ceil
class Solution:  # 36ms, początkowo zapomniałem o przypadku numRows==0
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        result = [[1],]
        for i in range(1, numRows):
            row = [1] * (i+1)
            for x in range(1, int(ceil((i+1)/2))):
                row[x] = row[~x] = result[-1][x-1] + result[-1][x]
            result.append(row)
        return result



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 1
        expected_output = [[1]]
        output = Solution().generate(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 2
        expected_output = [[1], [1,1]]
        output = Solution().generate(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 3
        expected_output = [[1],[1,1],[1,2,1]]
        output = Solution().generate(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = 4
        expected_output = [[1],[1,1],[1,2,1],[1,3,3,1]]
        output = Solution().generate(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = 5
        expected_output = [[1],[1,1],[1,2,1],[1,3,3,1], [1,4,6,4,1]]
        output = Solution().generate(input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)