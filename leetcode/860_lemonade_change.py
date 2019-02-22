#/usr/bin/env python3
import unittest

"""
At a lemonade stand, each lemonade costs $5. 

Customers are standing in a queue to buy from you, and order one at a time
(in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10,
or $20 bill.  You must provide the correct change to each customer, so that
the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.
"""

class Solution:
    # 52 ms (69.26%) - counting ch20
    # 48 ms (86.20%) - no counting ch20
    def lemonadeChange(self, bills: 'List[int]') -> 'bool':
        ch5 = ch10 = 0
        # no need to count ch20
        for v in bills:
            if v == 5:
                ch5 += 1
            elif v == 10:
                ch10 += 1
                ch5 -= 1
            else:
                if ch10 > 0:
                    ch10 -= 1
                    ch5 -= 1
                else:
                    ch5 -= 3
            if any((ch5 < 0, ch10 < 0)):
                return False
        return True


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [5,5,5,10,20]
        expected_output = True
        output = Solution().lemonadeChange(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [5,5,10]
        expected_output = True
        output = Solution().lemonadeChange(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [10,10]
        expected_output = False
        output = Solution().lemonadeChange(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
        expected_output = True
        output = Solution().lemonadeChange(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)