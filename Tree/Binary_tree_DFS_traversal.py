class Node:
    def __init__(self, data) -> None:
        self.data= data
        self.left: Node | None = None
        self.right: Node | None = None


def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.data, end=" ")
    in_order_dfs(node.right)

def pre_order_dfs(node):
    if node is None:
        return
    print(node.data, end=" ")
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)

def post_order_dfs(node):
    if node is None:
        return
    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(node.data, end=" ")

if __name__ == "__main__":
    # Creating the tree
    root: Node = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print("In-order DFS: ", end='')
    in_order_dfs(root)
    print("\nPre-order DFS: ", end='')
    pre_order_dfs(root)
    print("\nPost-order DFS: ", end='')
    post_order_dfs(root)