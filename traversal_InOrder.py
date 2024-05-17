class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, item):
    if root is None:
        return Node(item)
    else:
        if root.val < item:
            root.right = insert(root.right, item)
        else:
            root.left = insert(root.left, item)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")

# Example usage:
root = None
# keys = [50, 30, 20, 40, 70, 60, 80]
keys=[5,6,9,4,2,0,7]

# Insert keys into the tree
for key in keys:
    root = insert(root, key)

print("Inorder Traversal:")
inorder_traversal(root)

print("\n\nPreorder Traversal:")
preorder_traversal(root)

print("\n\nPostorder Traversal:")
postorder_traversal(root)
print()
