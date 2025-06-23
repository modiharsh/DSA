class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


def in_order_traversal(root):
    if root is None:
        return
    in_order_traversal(root.left)
    print(root.data, end=" ")
    in_order_traversal(root.right)

def insert(root, data):
    if root is None:
        return Node(data)
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left is None:
            node.left = Node(data)
            break
        else:
            queue.append(node.left)

        if node.right is None:
            node.right = Node(data)
            break
        else:
            queue.append(node.right)

    return root

def search(root, value):
    if root is None:
        return False
    
    if root.data == value:
        return True
    
    left_res: bool = search(root.left, value)
    right_res: bool = search(root.right, value)

    return left_res or right_res

def delete(root, value):
    if root is None:
        return
    
    queue = [root]
    target = None
    while queue:
        node = queue.pop(0)
        if node.data == value:
            target = node
            break
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    if not target:
        return root
    
    last_node = None
    last_parent = None

    queue = [(root, None)]
    
    while queue:
        curr, parent = queue.pop(0)
        last_node = curr
        last_parent = parent
        if curr.left:
            queue.append((curr.left, curr))
        if curr.right:
            queue.append((curr.right, curr))

    target.data = last_node.data  # type: ignore

    if last_parent:
        if last_parent.left == last_node:
            last_parent.left = None
        else:
            last_parent.right = None
    else:
        return None
    return root

    

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(1)

    print("Inorder traversal before insertion: ", end="")
    in_order_traversal(root)
    print()

    key = 6
    root = insert(root, key)

    print("Inorder traversal after insertion: ", end="")
    in_order_traversal(root)
    print()

    value = 3
    if search(root, value):
        print(f"{value} is found in the binary tree")
    else:
        print(f"{value} is not found in the binary tree")

    value = 4
    if search(root, value):
        print(f"{value} is found in the binary tree")
    else:
        print(f"{value} is not found in the binary tree")

    val_to_del = 6
    root = delete(root, val_to_del)

    print(f"Tree after deleting {val_to_del} (in-order): ", end="")
    in_order_traversal(root)
    print()