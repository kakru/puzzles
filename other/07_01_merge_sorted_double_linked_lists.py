#!/usr/bin/env python3

class ListNode:
    def __init__(self, value, pr=None, ne=None):
        self.value = value
        self.prev = pr
        self.next = ne
    def __repr__(self):
        return "<{}>".format(self.value)

def merge(A, B):
    R = ListNode(None)
    p1, p2, r = A, B, R
    while p1 and p2:
        if p1.value <= p2.value:
            r.next = p1
            r.next.prev = r
            p1 = p1.next
        else:  # p1.val > p2.val
            r.next = p2
            r.next.prev = r
            p2 = p2.next
        r = r.next
    # now at most one of A and B still has nodes to be merged
    if p1 is not None:
        r.next = p1
    else:  # p2 is not None
        r.next = p2
    r.next.prev = r
    return R.next  # skip the dummy node


nA1, nA5, nA7 = ListNode(1), ListNode(5), ListNode(7)
nB2, nB5, nB6 = ListNode(2), ListNode(5), ListNode(6)
nA1.next = nA5
nA5.next = nA7
nA7.prev = nA5
nA5.prev = nA1
A = nA1
nB2.next = nB5
nB5.next = nB6
nB6.prev = nB5
nB5.prev = nB2
B = nB2
R = merge(A, B)
r = R
while r:
    print(r.value)
    r = r.next
