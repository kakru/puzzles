# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # def leafs(self, root):  # iterative
    #     q = [root]
    #     lfs = []
    #     while q:
    #         p = q.pop()
    #         if not p.left and not p.right:
    #             lfs.append(p.val)
    #         else:
    #             if p.right: q.append(p.right)
    #             if p.left: q.append(p.left)
    #     return lfs

    def leafs(self, root):  # recursive
        def dfs(p, lst):
            if p:
                if p.left is None and p.right is None:
                    lst.append(p.val)
                else:
                    dfs(p.left, lst)
                    dfs(p.right, lst)
            return lst
        result = []
        return dfs(root, result)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.leafs(root1) == self.leafs(root2)


class Solution:  # LeetCode - using "yield from" trick
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))


t = TreeNode(3, 
        TreeNode(5,
            TreeNode(6),
            TreeNode(2,
                TreeNode(7),
                TreeNode(4)
            )
        ),
        TreeNode(1,
            TreeNode(9),
            TreeNode(8)
        )
    )

print(Solution().leafSimilar(t, t))
