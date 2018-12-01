#/usr/bin/env python3

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


# from collections import deque
# class Solution(object):
#     def preorder(self, root):
#         """
#         :type root: Node
#         :rtype: List[int]
#         """
#         if root is None: return []
#         q = deque([root])
#         result = []
#         while q:
#             p = q.popleft()
#             result.append(p.val)
#             q.extendleft(reversed(p.children))
#         return result

# Using stack (list) instead of deque
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None: return []
        q = [root]
        result = []
        while q:
            p = q.pop()
            result.append(p.val)
            q.extend(reversed(p.children))
        return result




tree = Node(1, [
    Node(3, [
        Node(5, []),
        Node(6, []),
    ]),
    Node(2, []),
    Node(4, []),
])

print(Solution().preorder(tree))