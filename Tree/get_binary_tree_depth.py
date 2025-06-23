class Node:
    def __init__(self, data) -> None:
        self.data= data
        self.left: Node | None = None
        self.right: Node | None = None

def get_height(root):
    if root is None:
        return -1

    l_height = get_height(root.left)
    r_height = get_height(root.right)

    return max(l_height, r_height) + 1

def get_height2(root):
    if root is None:
        return -1
    
    queue = [(root, 0)]
    max_depth = 0

    while queue:
        node, curr_depth = queue.pop(0)
        if node.left:
            queue.append((node.left, curr_depth+1))
        if node.right:
            queue.append((node.right, curr_depth+1))
        max_depth = max(max_depth, curr_depth)

    return max_depth

if __name__ == "__main__":
  
    # Representation of the input tree:
    #     12
    #    /  \
    #   8   18
    #  / \
    # 5   11
    root = Node(12)
    root.left = Node(8)
    root.right = Node(18)
    root.left.left = Node(5)
    root.left.right = Node(11)

    print(get_height(root))
    print(get_height2(root))