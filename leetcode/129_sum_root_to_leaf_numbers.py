#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.
"""

class Solution:  # 40 ms (62.07%)
    def sumNumbers(self, root: 'TreeNode') -> 'int':
        if not root: return 0
        results = []
        def helper(n, parent_value):
            value = parent_value * 10
            if n.left is None and n.right is None:  # leaf
                results.append(parent_value * 10 + n.val)
            if n.left: helper(n.left, parent_value * 10 + n.val)
            if n.right: helper(n.right, parent_value * 10 + n.val)
        helper(root, 0)
        return sum(results)

"""Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25."""

t = TreeNode(1,
        TreeNode(2),
        TreeNode(3))
print(Solution().sumNumbers(t))

"""Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026."""

t = TreeNode(4,
        TreeNode(9,
            TreeNode(5),
            TreeNode(1)),
        TreeNode(0))
print(Solution().sumNumbers(t))
