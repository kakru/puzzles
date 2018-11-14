#/usr/bin/env python3
import unittest

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        mails = set()
        for m in emails:
            user, domain = m.split('@')
            if '+' in user:
                user = user.split('+')[0]
            user = user.replace('.','')
            mails.add((user, domain))
        return len(mails)
                   
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        expected_output = 2
        output = Solution().numUniqueEmails(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)