class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def Deletion_Last_Node(self):
        Del=self.head
        while Del.link.link:
            Del=Del.link
        Del.link=None
    
    def Traversal(self):
        if self.head is None:
            print("Linked List is Empty:")

        else:
            temp=self.head

            while temp is not None:

                print(temp.data,"->",end="")
                temp=temp.link
            print()
SLL=SinglyLinkedList()
SLL.head=Node(11)
N2=Node(22)
N3=Node(33)
N4=Node(44)
SLL.head.link=N2
N2.link=N3
N3.link=N4
SLL.Deletion_Last_Node()
SLL.Traversal()