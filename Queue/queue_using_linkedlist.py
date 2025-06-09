class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node | None = None

class Queue:
    def __init__(self) -> None:
        self.front: Node | None = None
        self.rear: Node | None = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.front = self.rear = new_node
            return
        
        self.rear.next = new_node # type: ignore
        self.rear = new_node
        return

    def dequeue(self):
        if self.is_empty():
            
            print("Queue is empty")
            return
        temp_node: Node = self.front # type: ignore
        self.front = self.front.next # type: ignore
        if not self.front:
            self.rear = None

    def get_size(self):
        count = 0 
        curr = self.front
        while curr:
            count += 1
            curr = curr.next
        return count

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        curr: Node | None = self.front
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()



q = Queue()
print(f"Is empty : {q.is_empty()}")
q.enqueue(1)
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
print("Queue after enqueue: ", end="")
q.print_queue()
print(f"Queue size : {q.get_size()}")
q.dequeue()
print("Queue after dequeue: ", end="")
q.print_queue()
