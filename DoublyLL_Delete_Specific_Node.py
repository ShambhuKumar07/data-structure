class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def Appen_Method(self,item):
        New_Node=Node(item)
        if self.head is None:
            self.head=New_Node

        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next

            temp.next=New_Node
            New_Node.prev=temp

    def Display(self):
        if not self.head :
            print("Linked List is Empty")
            return
        else:
            temp=self.head
            while temp:
                print(temp.data,"<->",end="")
                temp=temp.next
            print()

    def DeleteSficpeciNode(self,elemet):
        current=self.head
        while current:
            if current.data==elemet:
                if current.prev:
                    current.prev.next=current.next

                else:
                    self.head=current.next

                if current.next:
                    current.next.prev=current.prev
                return
        
            current=current.next ## increment
        else:
            print(" Element is not present in linked list")
             

DLL=DoublyLinkedList()
DLL.Appen_Method(5)
DLL.Appen_Method(6)
DLL.Appen_Method(7)
DLL.Appen_Method(8)
DLL.Appen_Method(9)
# DLL.Display()

DLL.DeleteSficpeciNode(8)

DLL.Display()