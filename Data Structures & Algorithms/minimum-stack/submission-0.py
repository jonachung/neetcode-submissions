class MinStack:
    # have a stack = [] to be the stack
    # in the stack will be tuple (val, min)
    # when push into stack, the new min will be between min of top of stack vs val

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        newMin = val
        if self.stack:
            currentMin = self.stack[-1][1]
            newMin = min(newMin, currentMin)
        self.stack.append((val, newMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
