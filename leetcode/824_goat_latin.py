#/usr/bin/env python3
import unittest

class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        words = [w + 'ma' if w[0] in vowels else w[1:] + w[0] + 'ma' for w in S.split()]
        ret = []
        for i, w in enumerate(words):
            ret.append(w + 'a' * (i+1))
        return ' '.join(ret)

    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        words = [w + 'ma' + 'a' *(i+1)
                if w[0] in vowels
                else w[1:] + w[0] + 'ma' + 'a' *(i+1)
                for i, w in enumerate(S.split())]
        return ' '.join(words)

    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        return ' '.join([w + 'ma' + 'a' *(i+1)
                         if w[0] in set('aeiouAEIOU')
                         else w[1:] + w[0] + 'ma' + 'a' *(i+1)
                         for i, w in enumerate(S.split())])



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "I speak Goat Latin"
        expected_output = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
        output = Solution().toGoatLatin(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)