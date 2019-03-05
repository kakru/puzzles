#!/usr/bin/env python3
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# from collections import deque
# class Solution:  # 244 ms (82.62%)
#     def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
#         if not root: return 0
#         q, s = deque([root]), 0
#         while q:
#             p = q.popleft()
#             if not p: continue
#             if L <= p.val <= R: s += p.val
#             if p.val < R: q.append(p.right)
#             if p.val > L: q.append(p.left)
#         return s

class Solution:  # 236 ms (86.36%)
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        if not root: return 0
        q, s = [root], 0
        while q:
            p = q.pop()
            if not p: continue
            if L <= p.val <= R: s += p.val
            if p.val < R: q.append(p.right)
            if p.val > L: q.append(p.left)
        return s


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

print(Solution().rangeSumBST(n8, 0, 5))
print(Solution().rangeSumBST(n8, 3, 8))
print(Solution().rangeSumBST(n8, 0, 8))
