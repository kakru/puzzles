#/usr/bin/env python3
import unittest

class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        ## 36 ms (99.42%), 12.5 MB (100%) --> O(n)
        # return min(nums)
        #
        ## 36 ms (99.42%), 12.5 MB (100%) --> O(logn)
        i, j = 0, len(nums)-1
        if j < 0: return None
        while i < j:
            mid = (i+j) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        return nums[i]



class BasicTest(unittest.TestCase):
    def test_all(self):
        for test in [
            [[3,4,5,1,2], 1],
            [[4,5,6,7,0,1,2], 0],
            [[0,1], 0],
            [[1,0], 0],
            [[1,2,3], 1],
            [[5,1,2,3,4], 1],
        ]:
            self.assertEqual(Solution().findMin(test[0]), test[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)
