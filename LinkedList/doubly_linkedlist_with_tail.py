from typing import Any


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def traversal(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def find_size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def print_list(self, debug=False):
        curr=  self.head
        while curr:
            print(curr.data, end=" ")
            if debug:
                print(f"prev : {curr.prev.data if curr.prev else None}, \
                       next: {curr.next.data if curr.next else None}")
            curr = curr.next
        print()

    def insert_at_front(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            return
            
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node # type: ignore
        self.tail = new_node    

    def insert_at_pos(self, pos, val):
        new_node = Node(val)
        if pos < 1:
            return

        if pos == 1:
            if not self.head:
                self.head = self.tail = new_node
                return
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        
        curr = self.head
        for _ in range(1, pos-1):
            if not curr:
                return
            curr = curr.next

        if curr.next: # type: ignore
            curr.next.prev = new_node # type: ignore
        new_node.next = curr.next # type: ignore
        curr.next = new_node # type: ignore

        
    def delete_at_front(self):
        if not self.head:
            return
        temp_node = self.head
        head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            return
        
        if not self.head.next:
            return
        
        self.tail = self.tail.prev # type: ignore
        self.tail.next = None # type: ignore

        
    def delete_at_pos(self, pos):
        if not self.head:
            return
        
        if pos<1:
            return
        
        if pos==1:
            if not self.head.next:
                return
            self.head = self.head.next
            self.head.prev = None
            return
        
        curr = self.head
        for _ in range(1, pos):
            if not curr:
                return
            curr = curr.next
        if not curr:
            return
        
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev    
        return

    def reverse_list(self):
        if not self.head:
            return
        
        curr = self.head
        prev = None
        
        # Updating tail to the current head before reversing
        self.tail = self.head

        while curr:
            temp_node = curr.next
            curr.next = prev
            curr.prev = temp_node
            prev = curr
            curr = temp_node
        
        # Updating head to the new first node after reversal
        self.head = prev




if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 3
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    dll = DoublyLinkedList()
    dll.insert_at_front(1)
    dll.insert_at_end(3)
    dll.insert_at_pos(2,2)

    print("Traversal: ", end="")
    dll.traversal()

    print(f"Node count : {dll.find_size()}")

    dll.insert_at_front(0)
    print(f"After inserting 0 at front:", end=" ")
    dll.print_list()

    dll.insert_at_end(5)
    print(f"After inserting 5 at end:", end=" ")
    dll.print_list()

    dll.insert_at_pos(5, 4)
    print(f"After inserting at 4th pos:", end=" ")
    dll.print_list()

    dll.reverse_list()
    print(f"After reversing the list:", end=" ")
    dll.print_list(debug=True)
    dll.print_list()

    dll.delete_at_front()
    print(f"After deleting at front:", end=" ")
    dll.print_list()

    dll.delete_at_end()
    print(f"After deleting at end:", end=" ")
    dll.print_list()

    dll.delete_at_pos(2)
    print(f"After deleting at 2nd pos:", end=" ")
    dll.print_list()

    
