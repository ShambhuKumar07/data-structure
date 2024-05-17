class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
    
    def Traversal(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp=self.head

            while temp is not None:
                print(temp.data,"-->",end="")
                temp=temp.link
            print()
    def Insert_Node_in_between(self,Middele_node,data1):
        new_node=Node(data1)

        new_node.link=Middele_node.link
        Middele_node.link=new_node
    
obj=SinglyLinkedList()

obj.head=Node(111)
N1=Node(50)
N2=Node(60)
obj.head.link=N1
N1.link=N2

obj.Insert_Node_in_between(obj.head.link,"hsdhdshds")
obj.Traversal()