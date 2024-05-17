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
    def Delete_node_at_given_pos(self,pos):
        if pos<1:
            print("Invalid Postion")
            return
        if pos==1:
            self.head=self.head.link
            return
    
        curerent=self.head
        index=1
        while curerent and index<pos-1:
            curerent=curerent.link
            index +=1

        if curerent is None and curerent.link is None:
            print("Position out of Range")
            return
        curerent.link=curerent.link.link

SLL=SinglyLinkedList()
SLL.head=Node(500)
N2=Node(100)
N3=Node(300)
N4=Node(400)
SLL.head.link=N2
N2.link=N3
N3.link=N4

SLL.Delete_node_at_given_pos(1)
SLL.Traversal()