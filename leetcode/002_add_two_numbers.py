import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # check the length of each list, cause it's not guaranteed that they are equal length!
        size1 = 1
        p1 = l1
        while p1.next:
            size1 += 1
            p1 = p1.next
        size2 = 1
        p2 = l2
        while p2.next:
            size2 += 1
            p2 = p2.next
        # make lists equal in length, filling the mising digits with 0s
        while size1 != size2:
            if size1 > size2:
                p2.next = ListNode(0)
                p2 = p2.next
                size2 += 1
            else:
                p1.next = ListNode(0)
                p1 = p1.next
                size1 += 1
        # now lists are equal in length
        p1, p2 = l1, l2
        result = r = ListNode(0)  # a temporary node
        reminder = 0
        while p1:  # until the input lists are over
            val = p1.val + p2.val + reminder
            r.next = ListNode(val % 10)
            reminder = val // 10
            p1, p2, r = p1.next, p2.next, r.next
        if reminder > 0:
            r.next = ListNode(reminder)
        # forget the first node
        result = result.next
        return result




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
        a, b = [2,4,3], [5,6,4]
        expected_output = [7,0,8]
        a = Tests.create_list(a)
        b = Tests.create_list(b)
        ab = Solution().addTwoNumbers(l1=a, l2=b)
        ab = Tests.destroy_list(ab)
        self.assertEqual(ab, expected_output)

    def test_example_2(self):
        a, b = [1,8], [0]
        expected_output = [1,8]
        a = Tests.create_list(a)
        b = Tests.create_list(b)
        ab = Solution().addTwoNumbers(l1=a, l2=b)
        ab = Tests.destroy_list(ab)
        self.assertEqual(ab, expected_output)

    def test_example_3(self):
        a, b = [5], [5]
        expected_output = [0,1]
        a = Tests.create_list(a)
        b = Tests.create_list(b)
        ab = Solution().addTwoNumbers(l1=a, l2=b)
        ab = Tests.destroy_list(ab)
        self.assertEqual(ab, expected_output)


unittest.main(verbosity=2)

