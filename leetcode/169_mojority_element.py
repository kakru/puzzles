import unittest
from collections import Counter

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1
        # return sorted(nums)[int(len(nums)/2)]
        # 2
        # return Counter(nums).most_common(1)[0][0]
        # 3 Boyer-Moore algo with O(n) time and O(1) storage
        counter = 0
        for n in nums:
            if counter == 0:
                number, counter = n, 1
            elif n == number:
                counter += 1
            else:
                counter -= 1
        return number
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [3,2,3]
        expected_output = 3
        output = Solution().majorityElement(input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [2,2,1,1,1,2,2]
        expected_output = 2
        output = Solution().majorityElement(input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [3,3,4]
        expected_output = 3
        output = Solution().majorityElement(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)