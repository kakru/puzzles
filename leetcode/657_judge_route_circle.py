import unittest
from collections import Counter

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        mvs = Counter(moves)
        not_back_up_down = mvs['U'] - mvs['D']
        not_back_left_right = mvs['L'] - mvs['R']
        return not (not_back_up_down or not_back_left_right)
        
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 'UD'
        expected_output = True
        output = Solution().judgeCircle(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = 'LL'
        expected_output = False
        output = Solution().judgeCircle(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)