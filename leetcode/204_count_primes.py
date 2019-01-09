#/usr/bin/env python3
import unittest

# Quite slow solution.
# Would need to look deeper into 'Sieve of Eratoshenes' improvements...
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        primes = list(range(2, n))
        for j in range(2, n):
            if primes[j-2] == 0 or j*j > n: continue
            i = 2
            while j*i < n:
                primes[j*i-2] = 0
                i += 1
        return n - primes.count(0) - 2



class BasicTest(unittest.TestCase):
    def test_10(self):
        input_ = 10
        expected_output = 4
        output = Solution().countPrimes(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 3
        expected_output = 1
        output = Solution().countPrimes(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
