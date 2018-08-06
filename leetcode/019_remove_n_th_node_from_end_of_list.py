import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return self.val
    def __str__(self):
        return self.val


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # use two pointers, starting at head, and then move the second
        # one in a way that the two are separated by n elements.
        # Then iterate over the list, moving two pointers in parallel
        # until reaching the list end. Then the first pointer is showing
        # the element before the one to be removed.
        # Proceed with removing the element.
        p1, p2 = head, head
        for _ in range(n-1):
            p2 = p2.next
        if p2.next is None:  # it's the first element of list to be removed
            elem = head
            head = head.next
            del elem
            return head
        p2 = p2.next
        while p2.next is not None:  # move along the list until p1.next shows the element to be removed
            p1 = p1.next
            p2 = p2.next
        elem = p1.next
        p1.next = p1.next.next
        del elem
        return head
        

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

    def test_middle_elem(self):
        input_ = [1,2,3,4,5,6]
        element_to_remove_from_the_end = 3
        expected_output = [1,2,3,5,6]
        a = Tests.create_list(input_)
        a = Solution().removeNthFromEnd(head=a, n=element_to_remove_from_the_end)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_last_elem(self):
        input_ = [1,2,3,4,5,6]
        element_to_remove_from_the_end = 1
        expected_output = [1,2,3,4,5]
        a = Tests.create_list(input_)
        a = Solution().removeNthFromEnd(head=a, n=element_to_remove_from_the_end)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_first_elem(self):
        input_ = [1,2,3,4,5,6]
        element_to_remove_from_the_end = 6
        expected_output = [2,3,4,5,6]
        a = Tests.create_list(input_)
        a = Solution().removeNthFromEnd(head=a, n=element_to_remove_from_the_end)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_only_elem(self):
        input_ = [1]
        element_to_remove_from_the_end = 1
        expected_output = []
        a = Tests.create_list(input_)
        a = Solution().removeNthFromEnd(head=a, n=element_to_remove_from_the_end)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)



unittest.main(verbosity=2)