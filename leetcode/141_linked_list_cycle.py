import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Faster solution from leetcode:
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if head is None or head.next is None:
#             return False
#         slow = head
#         fast = head.next
#         while fast and fast.next:
#             if slow == fast:
#                 return True
#             slow = slow.next
#             fast = fast.next.next
#         return False

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        q = head
        p = head.next
        while p:
            if p == q:
                return True
            p = p.next
            if p == q:
                return True
            p = p.next
            q = q.next
        return False

        
def show_list(head):
    lst = []
    while head is not None:
        node = head
        lst.append(node.val)
        head = node.next
    return lst


class Tests(unittest.TestCase):
    @staticmethod
    def create_list(lst):
        head = None
        for element in reversed(lst):
            new_node = ListNode(element)
            new_node.next = head
            head = new_node
        return head
    
    @staticmethod
    def destroy_list(head):
        lst = []
        while head is not None:
            node = head
            lst.append(node.val)
            head = node.next
            del node
        return lst


    def test_helper_methods_6(self):
        a = [1,2,3,4,5,6]
        b = Tests.destroy_list(Tests.create_list(a))
        self.assertEqual(a, b)
    def test_helper_methods_1(self):
        a = [1]
        b = Tests.destroy_list(Tests.create_list(a))
        self.assertEqual(a, b)
    def test_helper_methods_0(self):
        a = []
        b = Tests.destroy_list(Tests.create_list(a))
        self.assertEqual(a, b)


    def test_example_1(self):  # usual
        input_ = [1,2,3,4,5]
        expected_output = False
        a = Tests.create_list(input_)
        a = Solution().hasCycle(head=a)
        b = expected_output
        self.assertEqual(b, expected_output)



unittest.main(verbosity=2)

