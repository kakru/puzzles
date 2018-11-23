#!/usr/bin/env python2
import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p, c, n = None, head, head.next
        while c:
            c.next = p
            p, c = c, n
            n = c.next if c else None
        return p

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:  # 0 or 1 element lists are palindromes
            return True
        # 1. measure list's length
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        if length == 2:
            return (head.val == head.next.val)
        elif length == 3:
            return (head.val == head.next.next.val)
        # 2. find the (k//2 + 1)-th element, and point head2 to it
        head2 = head
        for i in range(length//2):
            prev = head2
            head2 = head2.next
        # 3. reverse the second half of the list - O(n), with space complexity O(n)
        head2 = self.reverseList(head2)
        # 4. compare the first half of the list (elements 1..n//2) with the second part of the list, using head and head2 until head2 is showing to None - if there is any difference return False, otherwise True
        p, p2 = head, head2
        while p2:
            if p.val != p2.val:
                return False
            p, p2 = p.next, p2.next
        return True


    
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


    # def test_example_1(self):
    #     input_ = [1,2,3,4,5]
    #     expected_output = False
    #     a = Tests.create_list(input_)
    #     a = Solution().isPalindrome(head=a)
    #     self.assertEqual(a, expected_output)

    def test_example_2(self):
        input_ = [1,2,3,3,2,1]
        expected_output = True
        a = Tests.create_list(input_)
        a = Solution().isPalindrome(head=a)
        self.assertEqual(a, expected_output)



unittest.main(verbosity=2)

