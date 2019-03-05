#/usr/bin/env python3
import unittest

"""
Given a chemical formula (given as a string), return the count of each atom.
An atomic element always starts with an uppercase character, then zero or more
lowercase letters, representing the name.
1 or more digits representing the count of that element may follow if the
count is greater than 1. If the count is 1, no digits will follow. For
example, H2O and H2O2 are possible, but H1O2 is impossible.
Two formulas concatenated together produce another formula. For example,
H2O2He3Mg4 is also a formula.
A formula placed in parentheses, and a count (optionally added) is also
a formula. For example, (H2O2) and (H2O2)3 are formulas.
Given a formula, output the count of all elements as a string in the
following form: the first name (in sorted order), followed by its count
(if that count is more than 1), followed by the second name (in sorted order),
followed by its count (if that count is more than 1), and so on.
"""


from collections import Counter
from math import log10, ceil
class Solution:
    # very slow and overcomplicated... 180ms, the best solution ~35ms
    # TODO: to be improved
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        def count(f):  # --> returns a dict of elements where the values are counters
            if len(f) == 0: return {}
            p1 = f.find('(')
            if p1 > -1:  # there is a (...)
                # find the corresponding ')'
                stack_count = 1
                p2 = p1 + 1
                while stack_count > 0:
                    if f[p2] == ')': stack_count -= 1
                    elif f[p2] == '(': stack_count += 1
                    p2 += 1
                p2 -= 1
                p3 = p2
                while len(f) > p3 and f[p2+1:p3+3].isdigit():
                    p3 += 1
                c = int(f[p2+1:p3+2]) if f[p2+1:p3+2] else 1
                before = count(f[:p1]) if f[:p1] else {}
                inside = count(f[p1+1:p2])
                after = count(f[p3+2:]) if f[p3+2:] else {}
                summary = Counter(before) + Counter(after)
                while c > 0:
                    summary = summary + Counter(inside)
                    c -= 1
                return summary
            else:  # there is no (...)
                result = Counter()
                i = len(f) - 1
                m, elem = None, []
                while i >= 0:
                    if f[i].isdigit():
                        if elem:
                            result["".join(elem)] += m
                            m, elem = 1, []
                        if m is None:
                            m = int(f[i])
                        elif m == 0:
                            m = 10 * int(f[i])
                        else:
                            m += int(f[i]) * 10**ceil(log10(m+1))
                    else:
                        elem.insert(0, f[i])
                        if f[i].isupper():
                            result["".join(elem)] += m or 1
                            m, elem = None, []
                    i -= 1
                result["".join(elem)] += m or 1
            return result
        d = count(formula)
        if '' in d: del d['']
        return "".join(["{}{}".format(k, d[k]) if d[k]>1 else k for k in sorted(d.keys())])

## Best LeetCode solution, but it fails on one of the tests
# import collections
# class Solution:
#     def countOfAtoms(self, formula):
#         dic, coeff, stack, elem, cnt, i = collections.defaultdict(int), 1, [], "", 0, 0  
#         for c in formula[::-1]:
#             if c.isdigit():
#                 cnt += int(c) * (10 ** i)
#                 i += 1
#             elif c == ")":
#                 stack.append(cnt)
#                 coeff *= cnt
#                 i = cnt = 0
#             elif c == "(":
#                 coeff //= stack.pop()
#                 i = cnt = 0
#             elif c.isupper():
#                 elem += c
#                 dic[elem[::-1]] += (cnt or 1) * coeff
#                 elem = ""
#                 i = cnt = 0
#             elif c.islower():
#                 elem += c
#         return "".join(k + str(v > 1 and v or "") for k, v in sorted(dic.items()))


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = "H2O"
        expected_output = "H2O"
        output = Solution().countOfAtoms(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = "Mg(OH)2"
        expected_output = "H2MgO2"
        output = Solution().countOfAtoms(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = "K4(ON(SO3)2)2"
        expected_output = "K4N2O14S4"
        output = Solution().countOfAtoms(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = "OH"
        expected_output = "HO"
        output = Solution().countOfAtoms(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = "MgO2H2"
        expected_output = "H2MgO2"
        output = Solution().countOfAtoms(input_)
        self.assertEqual(output, expected_output)

    def test_6(self):
        input_ = "H50"
        expected_output = "H50"
        output = Solution().countOfAtoms(input_)
        self.assertEqual(output, expected_output)

    def test_7(self):
        input_ = "((N4)2(OB4))3"
        expected_output = "B12N24O3"
        output = Solution().countOfAtoms(input_)
        self.assertEqual(output, expected_output)

    def test_8(self):
        input_ = "H11He49NO35B7N46Li20"
        expected_output = "B7H11He49Li20N47O35"
        output = Solution().countOfAtoms(input_)
        self.assertEqual(output, expected_output)

    def test_9(self):
        input_ = "H11He"
        expected_output = "H11He"
        output = Solution().countOfAtoms(input_)
        self.assertEqual(output, expected_output)

    def test_10(self):
        input_ = "((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"
        expected_output = "B18900Be18984C4200H5446He1386Li33894N50106O22638"
        output = Solution().countOfAtoms(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)