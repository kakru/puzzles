class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        min_ = min(nums)
        max_ = max(nums)
        if min_ > 1: return 1
        A = [0] * (len(nums) + 1)
        A[0] = 1
        for x in nums:
            if x >= 0 and x <= len(nums):
                A[x] = 1
        if 0 not in A:
            return max_ + 1
        ret = A.index(0)
        return ret
