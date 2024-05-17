class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

def Insert(root,item):
    if root is None:
        return Node(item)
    else:
        if root.data < item:
            root.right=Insert(root.right,item)

        else:
            root.left=Insert(root.left,item)
    return root

# def In_Order_Traversal(root):
#     if root:
#         In_Order_Traversal(root.left)
#         print(root.data,end="")
#         In_Order_Traversal(root.right)

def Pre_Order(root):
    if root:
        print(root.data,end="")
        Pre_Order(root.left)
        Pre_Order(root.right)

root=None
keys=[5,6,9,4,2,0,7]

for key in keys:
    root=Insert(root,key)

Pre_Order(root)
print()