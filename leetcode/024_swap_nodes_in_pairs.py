#!/usr/bin/env python3
import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p, c, n = None, head, head.next
        while n:
            if p:
                c.next, n.next, p.next = n.next, c, n
            else:
                c.next, n.next, head = n.next, c, n
            if c and c.next:
                p, c, n = c, c.next, c.next.next
            else:
                break
        return head
        

    
def show(head):
    lst = []
    while head is not None:
        node = head
        lst.append(node.val)
        head = node.next
        del node
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
        input_ = [1,2,3,4]
        expected_output = [2,1,4,3]
        a = Tests.create_list(input_)
        a = Solution().swapPairs(head=a)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_2(self):
        input_ = [1,2]
        expected_output = [2,1]
        a = Tests.create_list(input_)
        a = Solution().swapPairs(head=a)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_3(self):
        input_ = [1]
        expected_output = [1]
        a = Tests.create_list(input_)
        a = Solution().swapPairs(head=a)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_4(self):
        input_ = []
        expected_output = []
        a = Tests.create_list(input_)
        a = Solution().swapPairs(head=a)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_5(self):
        input_ = [1,2,3]
        expected_output = [2,1,3]
        a = Tests.create_list(input_)
        a = Solution().swapPairs(head=a)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_6(self):
        input_ = [1,2,3,4,5]
        expected_output = [2,1,4,3,5]
        a = Tests.create_list(input_)
        a = Solution().swapPairs(head=a)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)


unittest.main(verbosity=2)

