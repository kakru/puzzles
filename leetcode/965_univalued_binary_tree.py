#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        val = root.val
        stack = [root]
        while stack:
            p = stack.pop()
            if p.val != val: return False
            if p.left: stack.append(p.left)
            if p.right: stack.append(p.right)
        return True


t = TreeNode(1,
        TreeNode(1,
            TreeNode(1),
            TreeNode(1)
        ),
        TreeNode(1,
            None,
            TreeNode(1)
        )
    )

print(Solution().isUnivalTree(t), True)

t = TreeNode(2,
        TreeNode(2,
            TreeNode(5),
            TreeNode(2)
        ),
        TreeNode(2)
    )

print(Solution().isUnivalTree(t), False)
