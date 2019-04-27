#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # def isEqual(tree1: TreeNode, tree2: TreeNode) -> bool:
        #     stack1, stack2 = [tree1], [tree2]
        #     while stack1 and stack2:
        #         p1, p2 = stack1.pop(), stack2.pop()
        #         if p1.val != p2.val:
        #             return False
        #         else:
        #             if bool(p1.left) ^ bool(p2.left):
        #                 return False
        #             if bool(p1.right) ^ bool(p2.right):
        #                 return False
        #             if p1.left:  # and p2.left:
        #                 stack1.append(p1.left)
        #                 stack2.append(p2.left)
        #             if p1.right:  # and p2.right:
        #                 stack1.append(p1.right)
        #                 stack2.append(p2.right)
        #     return True
        def isEqual(tree1: TreeNode, tree2: TreeNode) -> bool:
            if tree1 is None and tree2 is None:
                return True
            if bool(tree1) ^ bool(tree2):
                return False
            if tree1.val != tree2.val or \
                bool(tree1.left) ^ bool(tree2.left) or \
                bool(tree1.right) ^ bool(tree2.right):
                return False
            return isEqual(tree1.left, tree2.left) and isEqual(tree1.right, tree2.right)
        stack = [s]
        while stack:
            p = stack.pop()
            if p.val == t.val:
                if isEqual(p, t): return True
            if p.left: stack.append(p.left)
            if p.right: stack.append(p.right)
        return False


s1 = TreeNode(3,
        TreeNode(4,
            TreeNode(1),
            TreeNode(2)
        ),
        TreeNode(5))

s2 = TreeNode(3,
        TreeNode(4,
            TreeNode(1, TreeNode(0)),
            TreeNode(2)
        ),
        TreeNode(5))
t = TreeNode(4,
        TreeNode(1),
        TreeNode(2))

a = TreeNode(1, TreeNode(1))
b = TreeNode(1)

assert Solution().isSubtree(s1, t) == True
assert Solution().isSubtree(s2, t) == False
assert Solution().isSubtree(a, b) == True
