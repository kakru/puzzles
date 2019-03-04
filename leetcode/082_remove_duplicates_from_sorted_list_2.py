import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:  # 52 ms (53.91%)
    def deleteDuplicates(self, head):
        if not head or not head.next: return head  # empty, and 1-element lists are OK
        p = dummy = ListNode(None)
        dummy.next = head
        while p.next and p.next.next:
            if p.next.val == p.next.next.val:
                current_val = p.next.val
                while p.next and p.next.val == current_val: p.next = p.next.next
            else:
                p = p.next
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


    # def test_helper_methods_6(self):
    #     a = [1,2,3,4,5,6]
    #     b = Tests.destroy_list(Tests.create_list(a))
    #     self.assertEqual(a, b)
    # def test_helper_methods_1(self):
    #     a = [1]
    #     b = Tests.destroy_list(Tests.create_list(a))
    #     self.assertEqual(a, b)
    # def test_helper_methods_0(self):
    #     a = []
    #     b = Tests.destroy_list(Tests.create_list(a))
    #     self.assertEqual(a, b)


    def test_a_few_inputs(self):
        test_cases = [
            {'input': [1,1,2], 'output': [2]},
            {'input': [1,1,2,3,3], 'output': [2]},
            {'input': [1], 'output': [1]},
            {'input': [], 'output': []},
            {'input': [1,1,1,1,1] , 'output': []},
            {'input': [1,1,2], 'output': [2]},
            {'input': [1,1,1,1,1,2], 'output': [2]},
            {'input': [2,1,1,1,1,1], 'output': [2]},
            {'input': [1,2,3,3,3,3,4], 'output': [1,2,4]},
        ]
        for case in test_cases:
            i = case['input']
            o = case['output']
            a = Tests.create_list(i)
            a = Solution().deleteDuplicates(head=a)
            b = Tests.destroy_list(a)
            self.assertEqual(b, o)



unittest.main(verbosity=2)

