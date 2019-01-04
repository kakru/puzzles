#/usr/bin/env python3
import unittest

import math
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0,1,1,2]
        if num <= 3: return ans[:num+1]
        counter = 0
        for n in range(4, num+1):
            ans.append(1 + ans[counter])
            counter += 1
            if counter == math.ceil(len(ans)/2):
                counter = 0
        return ans



class BasicTest(unittest.TestCase):
    def test_2(self):
        input_ = 2
        expected_output = [0,1,1]
        output = Solution().countBits(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = 5
        expected_output = [0,1,1,2,1,2]
        output = Solution().countBits(input_)
        self.assertEqual(output, expected_output)

    def test_x(self):
        input_ = 30
        expected_output = [bin(i).count('1') for i in range(input_ + 1)]
        output = Solution().countBits(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
