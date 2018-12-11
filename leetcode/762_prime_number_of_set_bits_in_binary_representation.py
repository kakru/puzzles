#/usr/bin/env python3
import unittest

# class Solution:  # 464ms
#     def countPrimeSetBits(self, L, R):
#         """
#         :type L: int
#         :type R: int
#         :rtype: int
#         """
#         def count_bits(number):
#             return bin(number).count("1")
#         # the input is in range [1, 10^6], 10^6 can be expressed in 20 bits
#         # prime numbers < 20 are: 2, 3, 5, 7, 11, 13, 17, 19
#         primes = set([2, 3, 5, 7, 11, 13, 17, 19])
#         return [count_bits(x) in primes for x in range(L, R+1)].count(True)


class Solution:  # 344ms
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        # the input is in range [1, 10^6], 10^6 can be expressed in 20 bits
        # prime numbers < 20 are: 2, 3, 5, 7, 11, 13, 17, 19
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        count = 0
        for x in range(L, R+1):
            if bin(x).count("1") in primes:
                count += 1
        return count
        


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 6, 10
        expected_output = 4
        output = Solution().countPrimeSetBits(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 10, 15
        expected_output = 5
        output = Solution().countPrimeSetBits(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
