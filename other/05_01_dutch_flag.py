#!/usr/bin/env python3

def dutch(A):
    if len(A) < 2: return
    pivot = A[len(A)//2]
    print("pivot:", pivot)
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[j], A[i] = A[i], A[j]
                break
    for i in range(len(A)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if A[j] > pivot:
                A[j], A[i] = A[i], A[j]
                break

# a = [1,3,7,4,5,2,9,8,2]
# a = [0,1,2,0,2,1,1]
# a = [2,2,2,1,0,0,0]
# print(a)
# print(list(sorted(a)))
# dutch(a)
# print(a)


def variant_2(A, elements):
    elements = sorted(elements)
    counter = {e: 0 for e in elements}
    for i in range(len(A)): counter[A[i]] += 1
    pos = 0
    for typ in elements[:-1]:
        for i in range(pos, len(A)):
            if i > sum(counter[e] for e in elements[:typ]):
                break
            for j in range(i+1, len(A)):
                if A[j] == typ:
                    A[i], A[j] = A[j], A[i]
                    pos = i + 1
                    break

a = [1,2,3,4,1,1]
variant_2(a, (1,2,3,4))
print(a)
a = [2,3,3,3,3,3,3,4,4,4,4,1,2,2,1]
variant_2(a, (1,2,3,4))
print(a)
