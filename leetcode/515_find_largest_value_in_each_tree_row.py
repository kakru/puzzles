#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

from collections import defaultdict
class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [(root, 0)]
        nodes = defaultdict(list)
        while stack:
            p, lvl = stack.pop()
            nodes[lvl].append(p.val)
            if p.left: stack.append((p.left, lvl + 1))
            if p.right: stack.append((p.right, lvl + 1))
        return [max(nodes[lvl]) for lvl in nodes.keys()]


t = TreeNode(1,
        TreeNode(3,
            TreeNode(5),
            TreeNode(3)
        ),
        TreeNode(2,
            None,
            TreeNode(9))
    )

print(Solution().largestValues(t))