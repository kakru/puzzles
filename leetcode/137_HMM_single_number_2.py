#!/usr/bin/env python3
import unittest

# LeetCode advanced solution:
# class Solution:
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """ 
#         a = 0 
#         b = 0 
#         for c in nums: 
#             a, b = (a&~b&~c)|(~a&b&c), (~a&b&~c)|(~a&~b&c) 
#         return a|b  

# my solution with counting bits
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit_limit = 32
        bits = [[0] * bit_limit, # +
                [0] * bit_limit] # -
        for n in nums:
            if n < 0:
                sign = 1
                n *= -1
            else:
                sign = 0
            b = bin(n)[2:]
            for i, x in enumerate(reversed(b)):
                bits[sign][i] += 1 if x=='1' else 0
        bits = [[x%3 for x in bits[0]], # +
                [x%3 for x in bits[1]]] # -
        if any(bits[0]):  # non-negative number
            return int(''.join([str(x) for x in reversed(bits[0])]),2)
        else:
            return -int(''.join([str(x) for x in reversed(bits[1])]),2)


# with two XORs, for single numbers and for double numbers
# --> this doesn't work for negative numbers :-(
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1, x2 = [0,0], [0,0]
        for n in nums:
            if n<0:
                sign = 1
                n *= -1
            else: sign=0
            # x1 - store single appearances, x2 - store double appearances
            # 1. this is the first time
            if (x1[sign]^n) & (x2[sign]^n):
                x1[sign] ^= n
            # 2. this is the second time
            elif ~(x1[sign]^n) & (x2[sign]^n):
                x1[sign] ^= n
                x2[sign] ^= n
            # 3. this is the third time
            else:
                x2[sign] ^= n
        return x1[0] or -x1[1]




class BasicTest(unittest.TestCase):
    # def test_1(self):
    #     self.assertEqual(
    #         Solution().singleNumber([2,2,3,2]),
    #         3
    #     )

    # def test_2(self):
    #     self.assertEqual(
    #         Solution().singleNumber([0,1,0,1,0,1,99]),
    #         99
    #     )

    # def test_3(self):
    #     self.assertEqual(
    #         Solution().singleNumber([1,-4,-4,-4]),
    #         1
    #     )
    
    def test_3(self):
        self.assertEqual(
            Solution().singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]),
            -4
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)