class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

def Insert(root,item):
    if root is None:
        return Node(item)
    else:
        if root.data<item:
            root.right=Insert(root.right,item)
        else:
            root.left=Insert(root.left,item)
    return root

def Pre_Order(root):
    if root:
        print(root.data,end="")
        Pre_Order(root.left)
        Pre_Order(root.right)

root=None

key=[5,6,9,4,2,0,7]

for keys in key:
    root=Insert(root,keys)

Pre_Order(root)
print()
