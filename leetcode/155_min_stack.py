class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        min_element = self.getMin()
        if min_element is None or min_element > x:
            min_element = x
        self.__stack.append((x, min_element))

    def pop(self):
        """
        :rtype: void
        """
        self.__stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.__stack:
            return self.__stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.__stack:
            return self.__stack[-1][1]
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert(minStack.getMin() == -3)
minStack.pop();
assert(minStack.top() == 0)
assert(minStack.getMin() == -2)