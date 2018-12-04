#/usr/bin/env python3
import unittest

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = n%2
        while n:
            n>>=1
            if flag == n%2:
                return False
            flag = n%2
        return True



class BasicTest(unittest.TestCase):
    def test_all(self):
        inputs = [5, 7, 11, 10, 12]
        outputs = [True, False, False, True, False]
        for i, o in zip(inputs, outputs):            
            self.assertEqual(Solution().hasAlternatingBits(i), o)


if __name__ == '__main__':
    unittest.main(verbosity=2)
