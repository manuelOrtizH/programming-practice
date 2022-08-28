#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self.stack_pop = [] # "Stack"
        self.stack_push = [] # "Stack"

    def push(self, x: int) -> None:
        self.stack_push.append(x)

    def pop(self) -> int:
        if self.stack_pop:
            return self.stack_pop.pop()
        else:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
            return self.stack_pop.pop()

    def peek(self) -> int:
        if self.stack_pop:
            return self.stack_pop[-1]
        else:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
            return self.stack_pop[-1]

    def empty(self) -> bool:
        if not self.stack_pop and not self.stack_push:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()