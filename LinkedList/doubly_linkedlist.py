class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def forward_traversal(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def forward_recursive_traversal(head):
    if not head:
        return
    print(head.data, end=" ")
    forward_recursive_traversal(head.next)

def backward_traversal(tail):
    curr = tail
    while curr:
        print(curr.data, end=" ")
        curr = curr.prev
    print()

def backward_recursive_traversal(tail):
    if not tail:
        return
    print(tail.data, end=" ")
    backward_recursive_traversal(tail.prev)

def find_size(head):
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count

def print_list(head, debug=False):
    while head:
        print(head.data, end=" ")
        if debug:
            print(f"prev : {head.prev.data if head.prev else None}, next: {head.next.data if head.next else None}")
        head = head.next
    print()

def insert_at_front(head, val):
    new_node = Node(val)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

def insert_at_end(head, val):
    new_node = Node(val)
    curr = head
    while curr.next:
        curr = curr.next
    if curr:
        new_node.prev = curr
        curr.next = new_node
    return head

def insert_at_pos(head, pos, val):
    new_node = Node(val)
    if pos < 1:
        return

    if pos == 1:
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node
    
    curr = head
    for _ in range(1, pos-1):
        if not curr:
            return
        curr = curr.next

    if curr.next:
        curr.next.prev = new_node
    new_node.next = curr.next
    curr.next = new_node
    return head
    
def delete_at_front(head):
    if not head:
        return
    temp_node = head
    head = head.next
    if head:
        head.prev = None
    return head

def delete_at_end(head):
    if not head:
        return
    
    if not head.next:
        return
    
    curr = head
    while curr.next:
        curr = curr.next
    if curr.prev:
        curr.prev.next = None
        curr.prev = None
    return head
    
def delete_at_pos(head, pos):
    if not head:
        return
    
    if pos<1:
        return
    
    if pos==1:
        if not head.next:
            return
        head = head.next
        head.prev = None
        return head
    
    curr = head
    for _ in range(1, pos):
        if not curr:
            return head
        curr = curr.next
    if not curr:
        return head
    
    if curr.prev:
        curr.prev.next = curr.next
    if curr.next:
        curr.next.prev = curr.prev    
    return head

def reverse_list(head):
    if not head:
        return
    
    prev = None
    curr = head
    while curr:
        temp_node = curr.next
        if curr.next:
            curr.prev = curr.next
        curr.next = prev
        prev = curr
        curr = temp_node
    prev.prev = None
    return prev




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

    print("Forward Traversal: ", end="")
    forward_traversal(head)
    print("Forward Recursive Traversal: ", end="")
    forward_recursive_traversal(head)
    print()

    print("Backward Traversal: ", end="")
    backward_traversal(third)
    print("Backward Recursive Traversal: ", end="")
    backward_recursive_traversal(third)
    print()

    print(f"Node count : {find_size(head)}")

    head = insert_at_front(head, 0)
    print(f"After inserting at front:", end=" ")
    print_list(head)

    head = insert_at_end(head, 5)
    print(f"After inserting at end:", end=" ")
    print_list(head)

    head = insert_at_pos(head, 5, 4)
    print(f"After inserting at 4th pos:", end=" ")
    print_list(head)

    head = reverse_list(head)
    print(f"After reversing the list:", end=" ")
    print_list(head, debug=True)

    head = delete_at_front(head)
    print(f"After deleting at front:", end=" ")
    print_list(head)

    head = delete_at_end(head)
    print(f"After deleting at end:", end=" ")
    print_list(head)

    head = delete_at_pos(head, 2)
    print(f"After deleting at 2nd pos:", end=" ")
    print_list(head)

    


    # Use cases of doubly linkedlist:
    # Implementation of undo and redo functionality in text editors.
    # Cache implementation where quick insertion and deletion of elements are required.
    # Browser history management to navigate back and forth between visited pages.
    # Music player applications to manage playlists and navigate through songs efficiently.
    # Implementing data structures like Deque (double-ended queue) for efficient insertion and deletion at both ends.