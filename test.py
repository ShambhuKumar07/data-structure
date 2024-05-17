class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Tree:
    def Create_Node(self,item):

        return Node(item) 
    
    def Insert(self,node,data):
        if node is None:
            return self.Create_Node(data)
        if data<node.data:
            node.left=self.Insert(node.left,data)

        else:
            node.right=self.Insert(node.right,data)

        return node
    
    def In_Order(self,root):
        if root is not None:
            self.In_Order(root.left)
            print(root.data)
            self.In_Order(root.right)
    

tree=Tree()
root=tree.Create_Node(10)
# print(root.left)
# print(root.data)
# print(root.right)
tree.Insert(root,8)
tree.Insert(root,10)
tree.In_Order(root)
