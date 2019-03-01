import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    # def __lt__(self, other):
    #     return self.val < other.val

# from heapq import heappop, heappush
# class Solution:
#     def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
#         if not lists: return []
#         elif len(lists) == 1: return lists[0]
#         mins = []  # heap
#         result = r = ListNode(None)
#         for i, l in enumerate(lists):
#             if l: heappush(mins, (l.val, l, i))
#         while mins:
#             _, new_result_node, i = heappop(mins)
#             lists[i] = lists[i].next
#             if lists[i]: heappush(mins, (lists[i].val, lists[i], i))
#             r.next = new_result_node
#             r = r.next
#         return result.next

from heapq import heappop, heappush
class Solution:  # 72 ms (91.40%) <-- with no change in ListNode class (__lt__ would be helpful)
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        if not lists: return []
        elif len(lists) == 1: return lists[0]
        mins = []  # heap
        result = r = ListNode(None)
        for i, l in enumerate(lists):
            if l: heappush(mins, (l.val, i))
        while mins:
            _, i = heappop(mins)
            new_result_node = lists[i]
            lists[i] = lists[i].next
            if lists[i]: heappush(mins, (lists[i].val, i))
            r.next = new_result_node
            r = r.next
        return result.next


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
        input_ = [1,4,5], [1,3,4], [2,6]
        expected_output = [1,1,2,3,4,4,5,6]
        lsts = [Tests.create_list(x) for x in input_]
        c = Solution().mergeKLists(lsts)
        c = Tests.destroy_list(c)
        self.assertEqual(c, expected_output)


unittest.main(verbosity=2)

