#!/usr/bin/env python3
import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        p, size = head, 1
        while p.next:
            size += 1
            p = p.next
        k = k % size
        if not k: return head
        new_head = head
        for _ in range(size-k-1): new_head = new_head.next
        new_head.next, new_head = None, new_head.next
        p = new_head
        for _ in range(k-1): p = p.next
        p.next = head
        return new_head

        

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
        input_ = [1,2,3,4,5], 2
        expected_output = [4,5,1,2,3]
        a = Tests.create_list(input_[0])
        a = Solution().rotateRight(head=a, k=input_[1])
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_2(self):
        input_ = [0,1,2], 4
        expected_output = [2,0,1]
        a = Tests.create_list(input_[0])
        a = Solution().rotateRight(head=a, k=input_[1])
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_3(self):
        input_ = [1,2], 0
        expected_output = [1,2]
        a = Tests.create_list(input_[0])
        a = Solution().rotateRight(head=a, k=input_[1])
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_4(self):
        input_ = [1], 0
        expected_output = [1]
        a = Tests.create_list(input_[0])
        a = Solution().rotateRight(head=a, k=input_[1])
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)



unittest.main(verbosity=2)

