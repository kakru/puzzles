#!/usr/bin/env python3
import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:  # 40 ms (35.40%)
    def reverseBetween(self, head: 'ListNode', m: 'int', n: 'int') -> 'ListNode':
        if not head or n-m < 1: return head
        dummy = ListNode(None)
        dummy.next = head
        a = dummy
        for _ in range(m-1): a = a.next
        b = a.next
        for _ in range(n-m):
            c = b.next
            a.next, b.next, c.next = c, c.next, a.next
        return dummy.next


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


    def test_example_0(self):
        input_ = [], 1, 5
        expected_output = []
        a = Tests.create_list(input_[0])
        a = Solution().reverseBetween(a, input_[1], input_[2])
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_1(self):
        input_ = [1,2,3,4,5], 1, 5
        expected_output = [5,4,3,2,1]
        a = Tests.create_list(input_[0])
        a = Solution().reverseBetween(a, input_[1], input_[2])
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_2(self):
        input_ = [1,2,3,4,5], 1, 3
        expected_output = [3,2,1,4,5]
        a = Tests.create_list(input_[0])
        a = Solution().reverseBetween(a, input_[1], input_[2])
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)


    # def test_example_2(self):
    #     input_ = [1,2,3,4,5], 2, 5
    #     expected_output = [1,5,4,3,2]
    #     a = Tests.create_list(input_[0])
    #     a = Solution().reverseBetween(a, input_[1], input_[2])
    #     b = Tests.destroy_list(a)
    #     self.assertEqual(b, expected_output)



unittest.main(verbosity=2)

