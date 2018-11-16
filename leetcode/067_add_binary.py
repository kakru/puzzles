#/usr/bin/env python3
import unittest

class Solution:
    @staticmethod
    def bin2int(b):
        return sum([2**i * int(x) for i, x in enumerate(reversed(b))])
    @staticmethod
    def int2bin(i):
        if i == 0:
            return "0"
        b = []
        power = 0
        while i > 0:
            bit = i&1
            b.append(str(bit))
            i >>= 1  # //= 2
        return "".join(reversed(b))

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Python specific solution
        # return bin(int(a, 2) + int(b, 2))[2:]
        # And step by step
        return self.int2bin(
            self.bin2int(a) + self.bin2int(b)
        )

        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "11", "1"
        expected_output = "100"
        output = Solution().addBinary(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "1010", "1011"
        expected_output = "10101"
        output = Solution().addBinary(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)