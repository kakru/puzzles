#/usr/bin/env python3
import unittest

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # with extra space - using sets:
        if not len(nums):
            return []
        return list(set(range(1, max(max(nums), len(nums)) + 1)) - set(nums))

# The trick here is to realizie that the numbers are >= 1,
# Meaning we can use the numbers in existing array to inverse the sign
# (so store additional bit of information per number)
#
# I think the solution from LeetCode (below) works in that way.

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = list()
        # attendence check
        for i in range(0,len(nums)):
            val = abs(nums[i])-1
            if(nums[val] > 0):
                nums[val] = -nums[val]
            
        #put absentees
        for i in range(0,len(nums)):
            if(nums[i] > 0):
                ans.append(i+1)
        
        return ans

class BasicTest(unittest.TestCase):
    # def test_(self):
    #     input_ = []
    #     expected_output = []
    #     output = Solution().findDisappearedNumbers(input_)
    #     self.assertEqual(output, expected_output)

    def test_1(self):
        input_ = [4,3,2,7,8,2,3,1]
        expected_output = [5,6]
        output = Solution().findDisappearedNumbers(input_)
        self.assertEqual(output, expected_output)

    # def test_2(self):
    #     input_ = [1,1]
    #     expected_output = [2]
    #     output = Solution().findDisappearedNumbers(input_)
    #     self.assertEqual(output, expected_output)

    # def test_3(self):
    #     input_ = [1]
    #     expected_output = []
    #     output = Solution().findDisappearedNumbers(input_)
    #     self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)