class MyQueue:

    def __init__(self):
        self.out_stack = []  # 2 ,1
        self.in_stack = []  # 1, 2
        

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        

    def pop(self) -> int:
        
        if not self.out_stack:

            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        return len(self.out_stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()