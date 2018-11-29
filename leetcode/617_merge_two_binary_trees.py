#!/usr/bin/env python3
import unittest

from itertools import zip_longest
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return {'val':self.val, 'left':self.left, 'right':self.right}

    def __str__(self):
        return '[ ' + str(self.val) + ' ]'

class Solution:
    def mergeBranch(self, p1, p2):
        if p1 is None and p2 is None:
            return None
        elif p1 and p2:
            if p1.val is None and p2.val is None:
                value = None
            else:
                value = (p1.val or 0) + (p2.val or 0)
        elif p2:  # p1 is None
            value = p2.val
        else:     # p2 is None
            value = p1.val
        p3 = TreeNode(value)
        p3.left = self.mergeBranch(p1.left if p1 else None, p2.left if p2 else None)
        p3.right = self.mergeBranch(p1.right if p1 else None, p2.right if p2 else None)
        return p3
        
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.mergeBranch(t1, t2)


#  SHORTER SOLUTION from LeetCode:
# class Solution:
#     def mergeTrees(self, t1, t2):
#         """
#         :type t1: TreeNode
#         :type t2: TreeNode
#         :rtype: TreeNode
#         """
#         if t1 is None:
#             return t2
#         if t2 is not None:
#             t1.val += t2.val
#             t1.left = self.mergeTrees(t1.left, t2.left)
#             t1.right = self.mergeTrees(t1.right, t2.right)
#         return t1



t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.left.left = TreeNode(5)
t1.right = TreeNode(2)

t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.left.right = TreeNode(4)
t2.right = TreeNode(3)
t2.right.right = TreeNode(7)

a = Solution().mergeTrees(t1, t2)
print()