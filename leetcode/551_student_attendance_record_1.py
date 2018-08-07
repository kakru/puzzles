import unittest

class Solution:  # Very slow comparing to other submissions :( why?
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absences = 0
        day_min1, day_min2 = None, None
        for day in s:
            if day is 'A':
                absences += 1
                if absences == 2:
                    return False
            elif day is 'L' and day_min1 is 'L' and day_min2 is 'L':
                return False
            day_min2, day_min1 = day_min1, day
        return True

        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 'PPALLP'
        expected_output = True
        output = Solution().checkRecord(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 'PPALLL'
        expected_output = False
        output = Solution().checkRecord(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = 'LALL'
        expected_output = True
        output = Solution().checkRecord(input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)