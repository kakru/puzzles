#!/usr/bin/env python3

# quite slow... 404 ms (8.08%)

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = None
        self._count = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        p, i = self._head, 0
        while p is not None and i<index:
            p = p.next
            i += 1
        if i == index and p is not None:
            return p.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self._head
        self._head = new_node
        self._count += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self._count, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self._count: return
        if index == 0:
            self.addAtHead(val)
        else:  # index > 0 and index <= self._count
            p, i = self._head, 1
            while p.next is not None and i<index:
                p = p.next
                i += 1
            new_node = Node(val)
            p.next, new_node.next = new_node, p.next
            self._count += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0 and self._count >= 1:
            self._head = self._head.next
            self._count -= 1
        elif 0 < index < self._count:
            p = self._head
            for _ in range(1, index): p = p.next
            p.next = p.next.next
            self._count -= 1


# for debuging
def show(head):
    ret = []
    p = head
    while p is not None:
        ret.append(p.val)
        p = p.next
    return ret


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(3)
assert param_1 == -1
obj.addAtHead(3)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtTail(4)
print("-----------")
for i in range(5):
    print(obj.get(i))
print("-----------")
obj.addAtIndex(1, 10)
for i in range(5):
    print(obj.get(i))
print("-----------")
obj.deleteAtIndex(0)
for i in range(5):
    print(obj.get(i))
print("-----------")