class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

def search_key(head, key):
    # This will also work but best practice is to assign a copy of head
    # while head is not None:
    #     if head.data == key:
    #         return True
    #     head = head.next
    # return False

    curr = head
    while curr is not None:
        if curr.data == key:
            return True
        curr = curr.next
    return False

def count_nodes(head):
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    print(f"Total nodes in the list : {count}")

def insert_at_front(head, val):
    
    new_node = Node(val)
    new_node.next = head
    return new_node

def insert_at_end(head, val):
    new_node = Node(val)
    if not head:
        return new_node
    
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

def insert_at_pos(head, pos, val):
    new_node = Node(val)
    if pos < 1:
        return head
    
    if pos == 1:
        new_node.next = head
        return new_node
    
    curr = head
    for _ in range(1, pos-1):
        if not curr:
            break
        curr = curr.next

    if not curr:
        return head
    
    new_node.next = curr.next
    curr.next = new_node
    
    return head

def delete_at_front(head):
    if not head:
        return
    temp_node = head
    head = head.next
    del temp_node
    return head

def delete_at_end(head):
    if not head:
        return
    if not head.next:
        return
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head

def delete_at_pos(head, pos):
    if not head:
        return
    if pos < 1:
        return head
    
    curr = head
    if pos == 1:
        head = curr.next
        return head
    
    for _ in range(1, pos-1):
        if not curr.next:
            return head
        curr = curr.next
    
    if curr.next:
        curr.next = curr.next.next
    return head

def reverse_list(head):
    curr = head
    prev = None

    while curr:
        temp_node = curr.next
        curr.next = prev
        prev = curr
        curr = temp_node

    return prev
        

def main():

    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    # Example of traversing the node and printing
    print_list(head)

    head = Node(14)
    head.next = Node(21)
    head.next.next = Node(13)
    head.next.next.next = Node(30)
    head.next.next.next.next = Node(10)

    print(search_key(head, 14))
    print(search_key(head, 22))

    count_nodes(head)
    print("Original Linked List:", end=" ")
    print_list(head)
    head = insert_at_front(head, 5)
    print("After inserting Nodes at the front:", end=" ")
    print_list(head)

    head = insert_at_end(head, 35)
    print("After inserting Nodes at the end:", end=" ")
    print_list(head)

    head = insert_at_pos(head, 3, 12)
    print_list(head)
    head = insert_at_pos(head, 12, 44)
    print_list(head)
    head = insert_at_pos(head, 1, 2)
    print_list(head)
    head = delete_at_front(head)
    print_list(head)
    head = delete_at_end(head)
    print_list(head)
    head = delete_at_pos(head, 3)
    print_list(head)
    head = delete_at_pos(head, 10)
    print_list(head)
    head = delete_at_pos(head, 1)
    print_list(head)
    head = delete_at_pos(head, 5)
    print_list(head)

    head = reverse_list(head)
    print("After Reversing the list:", end=" ")
    print_list(head)


if __name__ == "__main__":
    main()