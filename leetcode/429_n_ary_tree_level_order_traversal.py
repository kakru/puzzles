#!/usr/bin/env python3

# Fastest solution from LeetCode:
# class Solution(object):
#     def levelOrder(self, root):
#         """
#         :type root: Node
#         :rtype: List[List[int]]
#         """
#         result, level = [], [root]
#         while root and level:
#             result += [node.val for node in level],
#             level = [child for node in level for child in node.children if child]
#         return result



# Runtime: 156 ms, faster than 23.25% of Python online submissions
from collections import deque, defaultdict
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        results = defaultdict(list)
        q = deque( [(root, 0)] )
        while q:
            p, level = q.popleft()
            results[level].append(p.val)
            for ch in p.children:
                q.append( (ch, level+1) )
        final = [
            results[level] for level in range(0, max(results.keys()) + 1)
        ]
        return final
        
    