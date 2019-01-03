#/usr/bin/env python3
import unittest

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = []
        if num == 0: return "0"
        elif num < 0: num += 2**32
        while num:
            m = num & 15  # m = num % 16
            num -= m
            # if m < 10:
            #     ans.append(chr(48+m))
            # else:
            #     ans.append(chr(87+m))
            ans.append(str(chr(87+m)) if m >= 10 else chr(48+m))
            num >>= 4  # num //= 16
        return "".join(reversed(ans))
        


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 26
        expected_output = "1a"
        output = Solution().toHex(input_)
        self.assertEqual(output, expected_output)

    def test_m1(self):
        input_ = -1
        expected_output = "ffffffff"
        output = Solution().toHex(input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)
