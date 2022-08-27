# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/min-stack/

 # Initializing a stack


class MinStack:

    def __init__(self):
        self.stack = [] #Stack
        self._min_values = [] #Stack
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self._min_values.append(val)
        else:
            min_val = self._min_values[-1] #peek
            if val < min_val:
                min_val = val
            self._min_values.append(min_val)
            self.stack.append(val)
    
             
    def pop(self) -> None:
        self._min_values.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min_values[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
