#/usr/bin/env python3
import unittest

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        elif x < 4: return 1
        left, right = 0, x
        while right - left > 1:
            mid = (left + right)//2
            if mid**2 > x:
                right = mid
            # elif mid**2 < x:
            elif mid**2 <= x:
                left = mid
            else:
                return mid
        # if (left**2 < x) and (right**2 > x):
        #     return left
        # else:
        #     return right
        return left
                    
        

class BasicTest(unittest.TestCase):
    # def test_1(self):
    #     input_ = 4
    #     expected_output = 2
    #     output = Solution().mySqrt(input_)
    #     self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 15
        expected_output = 3
        output = Solution().mySqrt(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)