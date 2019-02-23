import unittest


# class Solution:
#     def isPowerOfThree(self, n: 'int') -> 'bool':
#         while n % 3 == 0 and n > 1:
#             n /= 3
#         return (n == 1)

from math import log
class Solution:
    def isPowerOfThree(self, n: 'int') -> 'bool':
        if n <= 0: return False
        x = log(n, 3)
        return bool(3**int(round(x)) == n)



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 3**18
        expected_output = True
        output = Solution().isPowerOfThree(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)