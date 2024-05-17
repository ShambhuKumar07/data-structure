class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def Traversal(self):
        if self.head is None:
            print("Linked List is Empty ")
        else:
            temp=self.head

            while temp is not None:
                print(temp.data,"->",end="")
                temp=temp.link
            print()

    def Delete_First_Node(self):
        self.head=self.head.link
         

SLL=SinglyLinkedList()
SLL.head=Node(1)
N2=Node(22)
N3=Node(33)
N4=Node(44)

SLL.head.link=N2
N2.link=N3
N3.link=N4
SLL.Delete_First_Node()
# SLL.Delete_First_Node()
SLL.Traversal()

