#/usr/bin/env python3
import unittest

# import string
# class Solution:  # The fastest solution from LeetCode
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         trans = str.maketrans("", "", string.punctuation)
#         s_in = ((s.translate(trans)).replace(" ", "")).lower()
#         #s_in = (''.join([char for char in s if char.isdigit() or char.isalpha()])).lower()
#         return s_in == s_in[::-1]


class Solution:  # distance between "zero" and "P" is 32 !!
    def isPalindrome(self, s):
        # 97-122 a-z
        # 65-90 A-Z
        # 48-57 0-9
        """
        :type s: str
        :rtype: bool
        """
        s = list([ord(x) for x in s if x.isalnum()])
        if not s:
            return True
        i, j = 0, len(s)-1
        while i < j:
            ch1, ch2 = s[i], s[j]
            if ch1-ch2 not in (-32, 0, 32):
                return False
            elif (48 <= ch1 <= 57) ^ (48 <= ch2 <= 57):  # if not both are numbers
                return False
            i += 1
            j -= 1
        return True




class BasicTest(unittest.TestCase):
    # def test_1(self):
    #     input_ = "A man, a plan, a canal: Panama"
    #     expected_output = True
    #     output = Solution().isPalindrome(input_)
    #     self.assertEqual(output, expected_output)

    # def test_2(self):
    #     input_ = "race a car"
    #     expected_output = False
    #     output = Solution().isPalindrome(input_)
    #     self.assertEqual(output, expected_output)

    # def test_3(self):
    #     input_ = "racA a car"
    #     expected_output = True
    #     output = Solution().isPalindrome(input_)
    #     self.assertEqual(output, expected_output)

    # def test_4(self):
    #     input_ = ".,"
    #     expected_output = True
    #     output = Solution().isPalindrome(input_)
    #     self.assertEqual(output, expected_output)

    # def test_5(self):
    #     input_ = "0P"
    #     expected_output = False
    #     output = Solution().isPalindrome(input_)
    #     self.assertEqual(output, expected_output)

    # def test_6(self):
    #     input_ = "P"
    #     expected_output = True
    #     output = Solution().isPalindrome(input_)
    #     self.assertEqual(output, expected_output)

    def test_7(self):
        input_ = "1b1"
        expected_output = True
        output = Solution().isPalindrome(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)