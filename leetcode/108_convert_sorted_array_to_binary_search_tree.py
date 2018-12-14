#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:  # 108 ms
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        m = len(nums) // 2
        middle = TreeNode(nums[m])
        if m > 0:
            middle.left = self.sortedArrayToBST(nums[:m])
        if m < len(nums)-1:
            middle.right = self.sortedArrayToBST(nums[m+1:])
        return middle


# class Solution:  # 132 ms
#     def sortedArrayToBST(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: TreeNode
#         """
#         def create(nums):
#             if not nums: return None
#             m = len(nums) // 2
#             middle = TreeNode(nums[m])
#             if m > 0:
#                 middle.left = create(nums[:m])
#             if m < len(nums)-1:
#                 middle.right = create(nums[m+1:])
#             return middle
#         return create(nums)


t = Solution().sortedArrayToBST([-10,-3,0,5,9])
