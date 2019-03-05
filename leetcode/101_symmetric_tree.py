#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        def check(t1, t2):
            if not t1 and not t2: return True
            elif t1 and t2:
                return t1.val == t2.val and \
                    check(t1.left, t2.right) and check(t1.right, t2.left)
            return False
        return (root is None) or check(root.left, root.right)



n1 = \
TreeNode(1,
    TreeNode(2,
        TreeNode(3),
        None
    ),
    TreeNode(2,
        None,
        TreeNode(3))
)

print(Solution().isSymmetric(n1))
            



