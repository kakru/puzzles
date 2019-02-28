#!/usr/bin/env python3

# def can_reach(A):  # O(n), memory: O(n)
#     size = len(A)
#     R = [True] + [False] * (size-1)
#     for i in range(size):
#         if R[i] is False:
#             continue
#         elif i+A[i] >= size:
#             return True
#         for j in range(A[i]):
#             R[i+j+1] = True
#     return False

def can_reach(A):  # O(n), memory: O(1)
    size = len(A)
    how_far = 0
    for i in range(size):
        if i > how_far:
            return False
        how_far = max(how_far, A[i]+i)
        if how_far >= size:
            return True
    # return False

print(can_reach([3,3,1,0,2,0,1]))
print(can_reach([3,2,0,0,2,0,1]))
