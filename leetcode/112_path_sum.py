#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:  # 56 ms (46.10%)
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        if not root: return False
        def helper(n, so_far):
            if not n.left and not n.right:  # a leaf
                if so_far + n.val == sum:
                    return True
                else:
                    return False
            return bool(
                (n.left and helper(n.left, so_far + n.val)) or
                (n.right and helper(n.right, so_far + n.val)))
        return helper(root, 0)


#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1

t = TreeNode(5,
        TreeNode(4,
            TreeNode(11,
                TreeNode(7),
                TreeNode(2)
            )
        ),
        TreeNode(8,
            TreeNode(13),
            TreeNode(4,
                None,
                TreeNode(1)
            )
        )
    )
print(Solution().hasPathSum(t, 22))  # True

t = TreeNode(1, TreeNode(2))
print(Solution().hasPathSum(t, 0))  # False
print(Solution().hasPathSum(t, 1))  # False
print(Solution().hasPathSum(t, 3))  # True