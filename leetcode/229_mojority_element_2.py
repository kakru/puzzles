import unittest
from collections import Counter

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []
        c1 = c2 = 0
        n1 = n2 = None
        for n in nums:
            if c1 < c2:  # make sure n1 is not less popular than n2
                c1, c2 = c2, c1
                n1, n2 = n2, n1
            if c1 == 0 and n1 != n and n2 != n:
                n1 = n
                c1 = 1
            elif c2 == 0 and n1 != n and n2 != n:
                n2 = n
                c2 = 1
            elif n == n1:
                c1 += 1
            elif n == n2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        # let's check if the selected element pass the 1/3 condition
        results = []
        c1 = c2 = 0
        for n in nums:
            if n == n1:
                c1 += 1
            elif n == n2:
                c2 += 1
        if c1 > len(nums)/3:
            results.append(n1)
        if c2 > len(nums)/3:
            results.append(n2)
        return results
        

class BasicTest(unittest.TestCase):
    def test_0(self):
        input_ = []
        expected_output = []
        output = Solution().majorityElement(input_)
        self.assertEqual(output, expected_output)

    def test_1(self):
        input_ = [3,2,3]
        expected_output = [3]
        output = Solution().majorityElement(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1,1,1,3,3,2,2,2]
        expected_output = [1,2]
        output = Solution().majorityElement(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [1,1,1,3,3,3,3,3,2,2,2]
        expected_output = [3]
        output = Solution().majorityElement(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [1,1,3,3,3,3,3,2,2,2,2]
        expected_output = [3,2]
        output = Solution().majorityElement(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = [1]
        expected_output = [1]
        output = Solution().majorityElement(input_)
        self.assertEqual(output, expected_output)

    def test_6(self):
        input_ = [3,2,3,1]
        expected_output = [3]
        output = Solution().majorityElement(input_)
        self.assertEqual(output, expected_output)

    def test_7(self):
        input_ = [1,2,3]
        expected_output = []
        output = Solution().majorityElement(input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)