class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_in_empty_list(last, val):
    if last:
        return
    
    new_node = Node(val)
    new_node.next = new_node
    last = new_node
    return last

def print_list(last):
    if not last:
        return
    
    head = last.next

    while True:
        print(head.data, end=" ")
        head = head.next
        if head == last.next:
            break
    print()

def insert_at_front(last, val):
    new_node = Node(val)
    if not last:
        new_node.next = new_node
        return new_node
    
    new_node.next = last.next
    last.next = new_node
    return last
    
def insert_at_end(last, val):
    new_node = Node(val)
    if not last:
        new_node.next = new_node
        return new_node
    
    new_node.next = last.next
    last.next = new_node
    return new_node
    
def insert_at_pos(last, pos, val):
    new_node = Node(val)

    if not last:
        if pos != 1:
            return
        new_node.next = new_node
        return new_node
    
    if pos<1:
        return last
    
    curr = last.next
    for _ in range(1, pos-1):
        curr = curr.next
        if curr == last.next:
            return last
        
    new_node.next = curr.next
    curr.next = new_node

    if curr == last:
        last = new_node
    return last

def delete_at_front(last):
    if not last:
        return
    
    head = last.next
    if head == last:
        return
    last.next = head.next
    return last

def delete_at_end(last):
    if not last:
        return
    
    if not last.next:
        return
    
    head = last.next
    curr = head

    while curr.next != last:
        curr = curr.next
    curr.next = head
    last = curr
    return last

def delete_at_pos(last, pos):
    if not last:
        return
    
    if pos<1:
        return

    if pos == 1:
        last.next = last.next.next
        return last

    head = last.next
    curr = head

    for _ in range(1, pos-1):
        curr = curr.next
        if curr == last:
            return last
    
    if curr.next == last:
        last = curr
    curr.next = curr.next.next
    return last
    
def delete_val(last, key):
    if not last:
        return

    curr = last.next
    prev = last

    # The node to be deleted is the only node in the list
    if curr == last and curr.data == key:
        return None
    
    # The node to be deleted is the first node
    if curr.data == key:
        last.next = curr.next
        return last
    
    while curr != last and curr.data != key:
        prev = curr
        curr = curr.next

    if curr.data == key:
        prev.next = curr.next
        if curr == last:
            last = prev
    else:
        print(f"Node with data {key} not found")

    return last


if __name__ == "__main__":
    last = None

    # Insert a node into the empty list
    last = insert_in_empty_list(last, 1)

    # Print the list
    print("List after insertion: ", end="")
    print_list(last)

    # Create circular linked list: 2, 3, 4
    first = Node(2)
    first.next = Node(3)
    first.next.next = Node(4)
    last = first.next.next
    last.next = first

    print("Original list: ", end="")
    print_list(last)

    # Insert 5 at the beginning
    last = insert_at_front(last, 5)
    print("List after inserting 5 at the front: ", end="")
    print_list(last)

    last = insert_at_end(last, 6)
    print("List after inserting 6 at the end: ", end="")
    print_list(last)

    last = insert_at_pos(last, 2, 7)
    print("List after inserting 7 at 2nd pos: ", end="")
    print_list(last)

    last = delete_at_front(last)
    print("List after deleting at the front: ", end="")
    print_list(last)

    last = delete_at_end(last)
    print("List after deleting at the end: ", end="")
    print_list(last)

    last = delete_at_pos(last, 4)
    print("List after deleting at 1st pos: ", end="")
    print_list(last)

    last = insert_at_front(last, 5)
    print("List after inserting 5 at the front: ", end="")
    print_list(last)

    last = insert_at_end(last, 8)
    print("List after inserting 8 at the end: ", end="")
    print_list(last)

    last = delete_val(last, 4)
    print("List after deleting value 4: ", end="")
    print_list(last)

    last = delete_val(last, 7)
    print("List after deleting value 7: ", end="")
    print_list(last)

    # Applications of circular linkedlist
    # It is used for time-sharing among different users, typically through a Round-Robin scheduling mechanism.
    # In multiplayer games, a circular linked list can be used to switch between players. After the last player's turn, the list cycles back to the first player.
    # Circular linked lists are often used in buffering applications, such as streaming data, where data is continuously produced and consumed.
    # In media players, circular linked lists can manage playlists, this allowing users to loop through songs continuously.
    # Browsers use circular linked lists to manage the cache. This allows you to navigate back through your browsing history efficiently by pressing the BACK button