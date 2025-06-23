class Node:
    def __init__(self, data) -> None:
        self.data= data
        self.left: Node | None = None
        self.right: Node | None = None


def getSize(root):
    if root is None:
        return 0
    
    left_size = getSize(root.left)
    right_size = getSize(root.right)

    return left_size + right_size + 1
    
def getSize2(root):
    if root is None:
        return 0
    
    total_count = 1
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if curr.left:
            queue.append(curr.left)
            total_count += 1
        if curr.right:
            queue.append(curr.right)
            total_count += 1
    
    return total_count




if __name__ == "__main__":

# Constructed binary tree is
#         1
#        / \
#       2   3
#      / \
#     4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(getSize(root))
    print(getSize2(root))