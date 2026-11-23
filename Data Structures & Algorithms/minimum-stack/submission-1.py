class MinStack:

    def __init__(self):
        self.stack = []
        self.history = []
        self.min_result = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_result is None:
            self.min_result = self.stack[len(self.stack)-1]
        elif self.min_result > val:
            self.min_result = self.stack[len(self.stack)-1]

        self.history.append(self.min_result)

    def pop(self) -> None:
        self.stack.pop()
        self.history.pop()
        if (len(self.history)) != 0:
            self.min_result = self.history[len(self.history)-1]
        else:
            self.min_result = None

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min_result
