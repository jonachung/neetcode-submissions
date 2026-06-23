class MinStack:
    # Data structure will be a stack.
    # however stack will hold a tuple of (val, currentMin)
    # in push operation, if val is < stack[-1].currentMin, the currentMin for new tuple to push is val


    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            currentMin = self.stack[-1][1]
            if currentMin < val:
                self.stack.append((val, currentMin))
                return
        
        self.stack.append((val, val))
        return

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
