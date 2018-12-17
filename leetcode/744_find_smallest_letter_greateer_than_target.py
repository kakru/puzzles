#/usr/bin/env python3
import unittest

class Solution:  # O(N)
    # letters are sorted so it can be improved to O(log(N)) if needed
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for c in letters:
            if c > target:
                return c
        return letters[0]


class MultiTest(unittest.TestCase):
    def test_1(self):
        input_values = ["c", "f", "j"], "a"
        expected_output = "c"
        output = Solution().nextGreatestLetter(*input_values)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_values = ["c", "f", "j"], "c"
        expected_output = "f"
        output = Solution().nextGreatestLetter(*input_values)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_values = ["c", "f", "j"], "d"
        expected_output = "f"
        output = Solution().nextGreatestLetter(*input_values)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_values = ["c", "f", "j"], "g"
        expected_output = "j"
        output = Solution().nextGreatestLetter(*input_values)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_values = ["c", "f", "j"], "j"
        expected_output = "c"
        output = Solution().nextGreatestLetter(*input_values)
        self.assertEqual(output, expected_output)

    def test_6(self):
        input_values = ["c", "f", "j"], "k"
        expected_output = "c"
        output = Solution().nextGreatestLetter(*input_values)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
