
# many possible (interesting) solutions here:
# https://leetcode.com/articles/set-mismatch/

from collections import Counter
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        count = Counter(nums)
        return [count.most_common(1)[0][0], (range(1, size+1) - count.keys()).pop()]
        

print(Solution().findErrorNums([1,2,2,4]))