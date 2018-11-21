import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # if not head:
        #     return None
        p = head
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        while head and head.val == val:
            head = head.next
        return head

        
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
        val = 2
        expected_output = [1,3,4,5]
        a = Tests.create_list(input_)
        a = Solution().removeElements(head=a, val=val)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_2(self):  # last
        input_ = [1,2,3,4,5]
        val = 5
        expected_output = [1,2,3,4]
        a = Tests.create_list(input_)
        a = Solution().removeElements(head=a, val=val)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_3(self):  # first
        input_ = [1,2,3,4,5]
        val = 1
        expected_output = [2,3,4,5]
        a = Tests.create_list(input_)
        a = Solution().removeElements(head=a, val=val)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_4(self):  # only element, nothing to remove
        input_ = [1]
        val = 5
        expected_output = [1]
        a = Tests.create_list(input_)
        a = Solution().removeElements(head=a, val=val)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_5(self):  # only element, and to be removed
        input_ = [1]
        val = 1
        expected_output = []
        a = Tests.create_list(input_)
        a = Solution().removeElements(head=a, val=val)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_6(self):  # empty list
        input_ = []
        val = 5
        expected_output = []
        a = Tests.create_list(input_)
        a = Solution().removeElements(head=a, val=val)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_7(self):  # all elements to be removed
        input_ = [1,1]
        val = 1
        expected_output = []
        a = Tests.create_list(input_)
        a = Solution().removeElements(head=a, val=val)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)

    def test_example_8(self):  # 1,2,2,1 --> 1,1
        input_ = [1,2,2,1]
        val = 2
        expected_output = [1,1]
        a = Tests.create_list(input_)
        a = Solution().removeElements(head=a, val=val)
        b = Tests.destroy_list(a)
        self.assertEqual(b, expected_output)



unittest.main(verbosity=2)

