#/usr/bin/env python3
import unittest

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        count = len(strs)
        if count == 0:
            return ""
        shortest = min([len(x) for x in strs])
        index = 0
        while index < shortest:
            character = strs[0][index]
            for i in range(1, count):
                if character != strs[i][index]:
                    return strs[0][:index]
            index += 1
        return strs[0][:shortest]
        

class BasicTest(unittest.TestCase):
    # def test_1(self):
    #     input_ = ["flower","flow","flight"]
    #     expected_output = "fl"
    #     output = Solution().longestCommonPrefix(input_)
    #     self.assertEqual(output, expected_output)

    # def test_2(self):
    #     input_ = ["dog","racecar","car"]
    #     expected_output = ""
    #     output = Solution().longestCommonPrefix(input_)
    #     self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = ["aa", "a"]
        expected_output = "a"
        output = Solution().longestCommonPrefix(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)