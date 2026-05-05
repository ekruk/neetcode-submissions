class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.minimum = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minimum:
            self.minimum = val
        self.minstack.append(self.minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        if len(self.stack) == 0:
            self.minimum = float('inf')
        else:
            self.minimum = self.getMin()
        
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
