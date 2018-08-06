import unittest
from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domains = Counter()
        for cpd in cpdomains:
            c = cpd.split()
            count, domain = int(c[0]), c[1]
            while '.' in domain:
                domains[domain] += count
                domain = domain.split('.', 1)[1]
            domains[domain] += count
        return ['{} {}'.format(x[1], x[0]) for x in domains.items()]
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = ["9001 discuss.leetcode.com"]
        expected_output = ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
        output = Solution().subdomainVisits(input_)
        self.assertEqual(sorted(output), sorted(expected_output))
        

if __name__ == '__main__':
    unittest.main(verbosity=2)