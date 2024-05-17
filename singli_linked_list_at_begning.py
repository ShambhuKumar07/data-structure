class Node:
    def __init__(self,data):
        self.data=data
        self.link=None
    
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def Traversal(self):
        if(self.head is None):
            print("Linked List is Empty")
        else:
            Temp=self.head
            while(Temp is not None):
                print(Temp.data,"->",end="")
                Temp=Temp.link
            print()
    def Add_Element_At_Begining(self,data1):
        New_Node=Node(data1)
    
        New_Node.link=self.head
        self.head=New_Node

obj=SinglyLinkedList()
obj.head=Node(11)
Node1=Node(500)
Node2=Node(600)
Node3=Node(700)
obj.head.link=Node1
Node1.link=Node2
Node2.link=Node3
obj.Add_Element_At_Begining(55555)
obj.Traversal()