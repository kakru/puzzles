#/usr/bin/env python3
import unittest

class Solution:  # straightforward, step by step solution
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Python:
        # return str(int(num1) + int(num2))
        i, j = len(num1)-1, len(num2)-1
        rem = 0
        number = []
        while i >= 0 or j >= 0:
            if i >= 0:
                d1 = ord(num1[i]) - 48
            else:
                d1 = 0
            if j >= 0:
                d2 = ord(num2[j]) - 48
            else:
                d2 = 0
            s = d1 + d2 + rem
            number.append(chr((s % 10) + 48))
            rem = s // 10
            i -= 1
            j -= 1
        if rem > 0:
            number.append(chr(rem + 48))
        return "".join(reversed(number))


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "123", "456"
        expected_output = "579"
        output = Solution().addStrings(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "1", "9"
        expected_output = "10"
        output = Solution().addStrings(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
