import sys


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [None] * 10000
        self.min_values = [None] * 10000
        self.idx = -1

    def push(self, x: int) -> None:
        self.idx += 1
        min_value = min(x, self.min_values[self.idx-1]) if self.idx > 0 else x
        self.min_values[self.idx] = min_value
        self.stack[self.idx] = x

    def pop(self) -> None:
        if self.idx >= 0:
            val = self.stack[self.idx]
            self.idx -= 1
            return val
        return None

    def top(self) -> int:
        return self.stack[self.idx] if self.idx >= 0 else None

    def getMin(self) -> int:
        return self.min_values[self.idx]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)

print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())
