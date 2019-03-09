#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:  # 56 ms (81.52%)
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        if not root: return []
        results = []
        def helper(n, path, so_far_sum):
            path.append(n.val)
            so_far_sum += n.val
            if n.left is None and n.right is None:  # a leaf
                if so_far_sum == sum:
                    results.append(path[:])
            if n.left: helper(n.left, path, so_far_sum)
            if n.right: helper(n.right, path, so_far_sum)
            path.pop()
            # so_far_sum -= n.val  # not needed
        helper(root, [], 0)
        return results

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1

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
                TreeNode(5),
                TreeNode(1)
            )
        )
    )
print(Solution().pathSum(t, 22))  # [[5,4,11,2], [5,8,4,5]]
