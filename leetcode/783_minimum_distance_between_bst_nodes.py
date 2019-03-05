#!/usr/bin/env python3

# LeetCode: 783 == LeetCode: 530

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:  # 40 ms (46.02%)
    def minDiffInBST(self, root: 'TreeNode') -> 'int':
        # visit the nodes in-order -> a BSTree behaves like a sorted array
        # meaning we need to compare only neighboring values
        if not root: return None
        def inorder(n):
            if n.left: yield from inorder(n.left)
            yield n
            if n.right: yield from inorder(n.right)
        now = float("-inf")
        minimum = float("inf")
        for p in inorder(root):
            prev, now = now, p.val
            minimum = min(minimum, now-prev)
        return minimum
            
            
n8 = \
TreeNode(8,
    TreeNode(3,
        TreeNode(1),
        TreeNode(6,
            TreeNode(4),
            TreeNode(7)
        )
    ),
    TreeNode(10,
        None,
        TreeNode(14,
            TreeNode(13))
    )
)

print(Solution().minDiffInBST(n8))  # 3,4 --> 1, 6,7 --> 1
