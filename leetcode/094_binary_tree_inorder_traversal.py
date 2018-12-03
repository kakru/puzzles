#/usr/bin/env python3

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        # return '[{}-->L:{}, R:{}]'.format(self.val, self.left, self.right)
        return '[{}]'.format(self.val)


# working well, but seems it has repeated code
# class Solution:
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         result = []
#         q = []
#         c = root
#         while c:
#             q.append(c)
#             c = c.left
#         while q:
#             c = q.pop()
#             result.append(c.val)
#             if c.right:
#                 c = c.right
#                 while c:
#                     q.append(c)
#                     c = c.left
#         return result


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        q = []
        p = root
        while p or q:
            while p:
                q.append(p)
                p = p.left
            p = q.pop()
            result.append(p.val)
            p = p.right
        return result



tree = Node(4, 
            Node(2,
                Node(1),
                Node(3)),
            Node(6,
                Node(5),
                Node(7)),
           )

print(Solution().inorderTraversal(tree))