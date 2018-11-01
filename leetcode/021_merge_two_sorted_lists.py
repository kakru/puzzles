import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = r = ListNode(0)  # a temporary node, to be removed
        p1, p2 = l1, l2
        while p1 and p2:
            if p1.val <= p2.val:
                r.next = p1
                p1 = p1.next
            else:
                r.next = p2
                p2 = p2.next
            r = r.next
        # add the remaining list in the end of the result
        if not p1:
            r.next = p2
        else:
            r.next = p1
        return result.next  # we are skipping the first node

# class Solution:  # the fastest solution somebody submited
#     def mergeTwoLists(self, l1, l2):
#         if not l1 and not l2:
#             return None
#
#         if not l1:
#             return l2
#       
#         if not l2:
#             return l1
#       
#         if l1.val < l2.val:
#           
#             l1.next = self.mergeTwoLists(l1.next,l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1,l2.next)
#             return l2

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


    def test_example_1(self):
        input_ = [1,2,4], [1,3,4]
        expected_output = [1,1,2,3,4,4]
        a = Tests.create_list(input_[0])
        b = Tests.create_list(input_[1])
        c = Solution().mergeTwoLists(l1=a, l2=b)
        c = Tests.destroy_list(c)
        self.assertEqual(c, expected_output)

    def test_example_2(self):
        input_ = [1], [1,3,4]
        expected_output = [1,1,3,4]
        a = Tests.create_list(input_[0])
        b = Tests.create_list(input_[1])
        c = Solution().mergeTwoLists(l1=a, l2=b)
        c = Tests.destroy_list(c)
        self.assertEqual(c, expected_output)

    def test_example_3(self):
        input_ = [1], []
        expected_output = [1]
        a = Tests.create_list(input_[0])
        b = Tests.create_list(input_[1])
        c = Solution().mergeTwoLists(l1=a, l2=b)
        c = Tests.destroy_list(c)
        self.assertEqual(c, expected_output)



unittest.main(verbosity=2)

