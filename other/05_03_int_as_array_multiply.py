#!/usr/bin/env python3

def multiply(A, B):
    res = [0] * (len(A) + len(B))
    sign = (A[0] < 0) ^ (B[0] < 0)
    A[0], B[0] = abs(A[0]), abs(B[0])
    for i in range(len(A)):
        for j in range(len(B)):
            res[~(i+j+1)] += A[~i] * B[~j]
            res[~(i+j)] += res[~(i+j+1)] // 10
            res[~(i+j+1)] %= 10
    i = 0
    while i < len(res) and res[i] == 0: i += 1
    if not res[i:]:
        return [0]    
    if sign:
        res[i] *= -1
    return res[i:-1]  # why until -1 (?)


print(multiply([1,2,3], [1,0,0]))
print(multiply([9,2], [1,1]))
print(multiply([1,1], [1,0]))
print(multiply([1], [1]))
print(multiply([1], [0]))
