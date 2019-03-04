#!/usr/bin/env python3
import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:  # 52 ms (55.48%)
    def oddEvenList(self, head: 'ListNode') -> 'ListNode':
        split = [ListNode(None), ListNode(None)]  # evens, odds
        heads_of_evens, heads_of_odds = split[0], split[1]
        p, i = head, 1
        while p is not None:
            split[i].next = p
            split[i] = split[i].next
            p = p.next
            i ^= 1
        split[0].next = None
        split[1].next = heads_of_evens.next
        return heads_of_odds.next

        

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
        input_ = [1,2,3,4,5]
        expected_output = [1,3,5,2,4]
        a = Tests.create_list(input_)
        a = Solution().oddEvenList(head=a)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_2(self):
        input_ = [2,1,3,5,6,4,7]
        expected_output = [2,3,6,7,1,5,4]
        a = Tests.create_list(input_)
        a = Solution().oddEvenList(head=a)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)


unittest.main(verbosity=2)
