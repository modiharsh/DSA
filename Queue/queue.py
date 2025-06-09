class Queue:
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)
    
    def peek(self):
        if not self.items:
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def get_size(self):
        return len(self.items)
    
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue:", my_queue.items)  # Output: Queue: [1, 2, 3]
print("Dequeue:", my_queue.dequeue())  # Output: Dequeue: 1
print("Queue after dequeue:", my_queue.items)  # Output: Queue after dequeue: [2, 3]
print("Peek:", my_queue.peek()) # Output: Peek: 2
print("Is empty:", my_queue.is_empty())  # Output: Is empty: False
print("Size:", my_queue.get_size())  # Output: Size: 2