class Node:
    def __init__(self, data) -> None:
        self.data= data
        self.left: Node | None = None
        self.right: Node | None = None

def bfs(root):
    if root is None:
        return
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    # Creating the tree
    root: Node = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print("Level order: ", end='')
    bfs(root)
