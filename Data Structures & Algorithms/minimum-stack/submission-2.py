class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        rev = [] 
        ret = float("inf")
        while self.stack:
            t = self.stack.pop()
            rev.append(t)
            ret = min(ret,t)
        while rev:
            self.stack.append(rev.pop())
        return ret
