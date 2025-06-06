from collections import deque

class Stack:
    def __init__(self) -> None:
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
s = Stack()
print(s.peek())
s.push(5)
s.push(10)
s.push(20)
print(s.peek())
print(s.is_empty())
print(s.size())
s.pop()
print(s.peek())