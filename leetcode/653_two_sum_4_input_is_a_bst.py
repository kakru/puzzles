#/usr/bin/env python3
import unittest

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:  # recursive DFS, 100ms
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        seen = set()
        def dfs(node):
            if node is None:
                return False
            elif node.val in seen:
                return True
            else:
                seen.add(k-node.val)
                if dfs(node.left) or dfs(node.right):
                    return True
            return False
        return dfs(root)
        


t = TreeNode(5,
        TreeNode(3,
            TreeNode(2),
            TreeNode(4)
        ),
        TreeNode(6,
            None,
            TreeNode(7)
        )
    )


print(Solution().findTarget(t, 9))  # should be True
print(Solution().findTarget(t, 28))  # should be False
