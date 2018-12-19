class TreeNode:  # the original solution doesn't provide the TreeNode structure
    def __init__(self, value):
        self.value = value
        self.left = left
        self.right = right

class Solution:  # O(n^2) - recursive, 148 ms (faster than 94.02%)
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0: return None
        maximum = max(nums)
        max_index = nums.index(maximum)
        n = TreeNode(maximum)
        n.left = self.constructMaximumBinaryTree(nums[:max_index])
        n.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return n


# TODO: better than O(n^2)


t = Solution().constructMaximumBinaryTree([3,2,1,6,0,5])
print(t)
