#/usr/bin/env python3
import unittest

"""
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.
Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.
Given a non-empty string S and a number K, format the string according to the rules described above.
"""

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        v = S.replace("-", "").upper()
        n, m = divmod(len(v), K)
        parts = [ v[m + i * K: m + (i+1) * K] for i in range(n) ]
        if m: parts.insert(0, v[:m])
        return "-".join(parts)

        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "5F3Z-2e-9-w", 4
        expected_output = "5F3Z-2E9W"
        # Explanation: The string S has been split into two parts, each part has 4 characters.
        # Note that the two extra dashes are not needed and can be removed.
        output = Solution().licenseKeyFormatting(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "2-5g-3-J", 2
        expected_output = "2-5G-3J"
        # Explanation: The string S has been split into three parts, each part has
        # 2 characters except the first part as it could be shorter as mentioned above.
        output = Solution().licenseKeyFormatting(*input_)
        self.assertEqual(output, expected_output)




if __name__ == '__main__':
    unittest.main(verbosity=2)
