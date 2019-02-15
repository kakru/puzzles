#1/usr/bin/env python3

class Solution:  # 44 ms (faster than 95.25%), 13.2 MB (less than 100%)
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        if not nums: return None
        s = m = nums[0]
        for n in nums[1:]:
            s = max(s+n, n)
            m = max(m, s)
        return m

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))