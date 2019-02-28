#!/usr/bin/env python3

def longest_subarray_of_equal(A):
    maximum = 0
    value = value_at = None
    for i, v in enumerate(A):
        if v != value:
            value, value_at = v, i
        maximum = max(maximum, i-value_at+1)
    return maximum


print(longest_subarray_of_equal([1,2,2,1,6,6,6,0]))
print(longest_subarray_of_equal([1,2,2]))
print(longest_subarray_of_equal([1,2]))
print(longest_subarray_of_equal([]))
print(longest_subarray_of_equal([5,5,2,5,5,0,5,5,5,5]))
