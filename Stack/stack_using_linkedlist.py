class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None


class Stack:
    def __init__(self) -> None:
        self.head: Node | None = None

    def is_empty(self):
        return self.head is None

    def push(self, val):
        new_node = Node(val)
        if not new_node:
            print("Stack Overflow")
            return
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return
        temp = self.head
        self.head = self.head.next # type: ignore
        del temp

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return float('-inf')
        return self.head.data # type: ignore
    
    # Creating a stack
s = Stack()

# Push elements onto the stack
s.push(11)
s.push(22)
s.push(33)
s.push(44)

# Print top element of the stack
print("Top element is", s.peek())

# removing two elemements from the top
print("Removing two elements...");
s.pop()
s.pop()

# Print top element of the stack
print("Top element is", s.peek())

    

        