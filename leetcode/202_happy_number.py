#/usr/bin/env python3
import unittest

# class Solution:  # 52 ms (47.41%)
#     @staticmethod
#     def digits(n):
#         return tuple(sorted(int(x) for x in str(n)))
#     def isHappy(self, n: 'int') -> 'bool':
#         number, seen = n, set()
#         while True:
#             d = self.digits(number)
#             if sum(d) == 1:
#                 return True
#             elif d in seen:
#                 return False
#             else:
#                 seen.add(d)
#                 number = sum(x*x for x in d)

class Solution:  # 52 ms (47.41%)
    def isHappy(self, n: 'int') -> 'bool':
        def parse(n):
            return sum(int(x)**2 for x in str(n))
        fast = parse(n)
        while fast != n:
            n, fast = parse(n), parse(parse(fast))
        return n == 1
        


class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            [19, True],
            [1019, False],
            [5555, True],
        ]:
            self.assertEqual(Solution().isHappy(test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)