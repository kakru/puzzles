#!/usr/bin/env python3
import unittest
"""
This problem was asked by Google.
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.
For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
Do this in O(N) time and O(1) space.
"""

def solution(A):
    bit_limit = 32
    bits = [
        [0] * bit_limit,  # positive 
        [0] * bit_limit   # negative
    ]
    for n in A:
        if n<0:  # negative 
            sign = 1    
            n *= -1
        else:  # positive
            sign = 0
        b = bin(n)[2:]
        for i, x in enumerate(reversed(b)):
            bits[sign][i] += 1 if x=='1' else 0
    bits = [[x%3 for x in bits[0]],
            [x%3 for x in bits[1]]]
    if any(bits[0]):
        number = int(''.join(str(x) for x in reversed(bits[0])), 2)
    else:
        number = -int(''.join(str(x) for x in reversed(bits[1])), 2)
    return number




class BasicTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            solution([6, 1, 3, 3, 3, 6, 6]),
            1
        )

    def test_2(self):
        self.assertEqual(
            solution([13, 19, 13, 13]),
            19
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)