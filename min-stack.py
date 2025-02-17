"""
the idea behind this question is to keep another stack alongside the current stack 
that always keeps track of the minimum number. For every new value pushed, we push 
the smaller value between the new value and the top of the minStack into the minStack.
This allows us to keep track of the minimum number even if we pop the min number, since
we would just pop from the minStack as well.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:

        if self.stack:
            newVal = min(val, self.minStack[-1])
        else:
            newVal = val

        self.stack.append(val)
        self.minStack.append(newVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

    def print(self) -> None:
        print(self.stack)


minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
