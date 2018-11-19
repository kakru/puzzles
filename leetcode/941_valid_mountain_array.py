#/usr/bin/env python3
import unittest

# Very ugly solution...

class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        size = len(A)
        if size < 3:
            return False
        diff = [A[i]-A[i-1] for i in range(1, size)]
        if 0 in diff:
            return False
        diff = [True if x > 0 else False for x in diff]
        if all(diff) or not any(diff):
            return False
        first_False = diff.index(False)
        if first_False == -1 or first_False == size-1 or any(diff[first_False:]):
            return False
        return True
            
                

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,3,2,1]
        expected_output = True
        output = Solution().validMountainArray(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1,3,2]
        expected_output = True
        output = Solution().validMountainArray(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [3,5,5]
        expected_output = False
        output = Solution().validMountainArray(input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [0,3,2,1]
        expected_output = True
        output = Solution().validMountainArray(input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = [0,1,2,3,4,5,6,7,8,9]
        expected_output = False
        output = Solution().validMountainArray(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)