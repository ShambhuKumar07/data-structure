class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def Add_Last(self,element):
        New_Node=Node(element)
        if self.head is None:
            self.head=New_Node
        else:
            current=self.head
            while current.next is not None:
                current=current.next

            current.next=New_Node

            New_Node.prev=current

    def Display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<->",end="")
                temp=temp.next
            print()

DLL=DoublyLinkedList()
DLL.Add_Last(20)
DLL.Add_Last(200)
DLL.Add_Last(2000)
DLL.Add_Last(20000)

DLL.Display()
