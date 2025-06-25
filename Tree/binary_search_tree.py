class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None

def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end=" ")
    in_order(node.right)

def insert(root, val):
    if root is None:
        return Node(val)
    
    if root == val:
        return root
    
    if root.data > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def insert_iteratively(root, val):
    if root is None:
        return Node(val)
    
    parent: Node | None = None
    curr= root
    while curr is not None:
        parent = curr
        if curr.data > val:
            curr = curr.left
        elif curr.data < val:
            curr = curr.right
        else:
            return root
        
    if parent.data > val:  # type: ignore
        parent.left = Node(val) # type: ignore
    else:
        parent.right = Node(val) # type: ignore

    return root

def search(root, val):
    if root is None or root.data == val:
        return root
    
    if root.data < val:
        return search(root.right, val)
    else:
        return search(root.left, val)    

def delete(root, val):
    def get_successor(curr):
        curr = curr.right
        while curr is not None and curr.left is not None:
            curr= curr.left
        return curr

    if root is None:
        return root
    
    if root.data > val:
        root.left = delete(root.left, val)
    elif root.data < val:
        root.right = delete(root.right, val)
    else:
        # If root matches with the given key

        # Cases when root has 0 children or 
        # only right child
        if root.left is None:
            return root.right
        # When root has only left child
        if root.right is None:
            return root.left
        # When both children are present
        succ = get_successor(root)
        root.data = succ.data
        root.right = delete(root.right, succ.data)

    return root
        

    
    

if __name__ == "__main__":
  
    # Creating the following BST
    #      50
    #     /  \
    #    30   70
    #   / \   / \
    #  20 40 60 80
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)   
    r = insert(r, 80)

    in_order(r)
    print()
    r= insert_iteratively(r, 10)

    in_order(r)
    print()
    print(f"Node 19 {'Found' if search(r, 19) else 'Not Found'}")
    print(f"Node 80 {'Found' if search(r, 80) else 'Not Found'}") 

    r: Node | None = delete(r, 50)
    in_order(r)
    print()