#/usr/bin/env python3
import unittest

import re
class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        size = len(logs)
        digit_log = re.compile('^[a-z0-9]+ [0-9 ]*$')
        logs_digits_only = [bool(digit_log.match(x)) for x in logs]
        logs_1 = sorted(
            [logs[i] for i in range(size) if not logs_digits_only[i]],
            key=lambda x: ' '.join(x.split()[1:] + [x[0]])
        )
        logs_2 = [logs[i] for i in range(size) if logs_digits_only[i]]
        return logs_1 + logs_2
                       
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
        expected_output = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
        output = Solution().reorderLogFiles(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]
        expected_output = ["5 m w","j mo","t q h","g 07","o 2 0"]
        output = Solution().reorderLogFiles(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)