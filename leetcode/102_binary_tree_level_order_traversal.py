#!/usr/bin/env python3
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# LeetCode - 36ms:
# class Solution:
#     def levelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         ans=[]
#         level=[root]
#         while root and level:
#             ans.append([node.val for node in level])
#             LRpair=[(node.left, node.right) for node in level]
#             level=[node for LR in LRpair for node in LR if node]
#         return ans

class Solution:  # 64ms
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        levels = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            p, level = q.popleft()
            levels[level].append(p.val)
            if p.left:
                q.append((p.left, level+1))
            if p.right:
                q.append((p.right, level+1))
        return [lvl for lvl in levels.values()]


# LeetCode example
n3 = TreeNode(3)
n9 = TreeNode(9)
n20 = TreeNode(20)
n15 = TreeNode(15)
n7 = TreeNode(7)
n3.left = n9
n3.right = n20
n20.left = n15
n20.right = n7
print(Solution().levelOrder(n3))
