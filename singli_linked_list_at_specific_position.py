class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def Insert_at_specific_position(self,pos,item):
        New_Node=Node(item)
        if pos==1:
            New_Node.link=self.head
            self.head=New_Node
        else:
            Current=self.head
            count=1
            while Current is not None and count<pos-1:
                Current=Current.link
                count +=1

            if(Current is None):
                print("Positioon Out of Range")
                return
            
            New_Node.link=Current.link

            Current.link=New_Node

    def Traversal(self):
        if self.head is None:
            print("Linked List is Empty ")
        else:
            temp=self.head
            while temp is not None:

                print(temp.data)
                temp=temp.link

SLL=SinglyLinkedList()
SLL.head=Node(50)

N2=Node(60)
N3=Node(70)
N4=Node(80)
SLL.head.link=N2
N2.link=N3
N3.link=N4
# SLL.Insert_at_specific_position(2,888)
SLL.Insert_at_specific_position(1,888)
# SLL.Insert_at_specific_position(0,88008)
SLL.Traversal()