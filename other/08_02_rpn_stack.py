#!/usr/bin/env python3

def RPN(L):  # Reverse Polish notation
    op = {"+": lambda a,b: a+b,
          "-": lambda a,b: a-b,
          "*": lambda a,b: a*b,
          "/": lambda a,b: a/b}
    op_keys = set(op.keys())
    stack = []
    for x in L:
        if x not in op_keys:
            stack.append(x)
        else:
            a = stack.pop()
            b = stack.pop()
            result = op[x](a, b)
            stack.append(result)
    return stack.pop()


print(RPN([3, 4, "+", 2, "*", 1, "+"]))
print(RPN([15, 7, 1, 1, "+", "-", "/", 3, "*", 2, 1, 1, "+", "+", "-"]))