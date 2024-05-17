class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def Append_method(self,item):
        New_Node=Node(item)
        if self.head is None:
            self.head=New_Node

        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next

            temp.next=New_Node
            New_Node.prev=temp
    def DeleteLastNode(self):
        if self.head is not None:
            temp=self.head
            while temp.next:
                temp=temp.next

            if temp.prev:
                temp.prev.next=None
            else:
                self.head=None

    def Display(self):
        if not self.head:
            print("Linked List is Empty")
            return 
        else:
            temp=self.head
            while temp:
                print(temp.data,"<->",end="")
                temp=temp.next

            print()

DLL=DoublyLinkedList()
DLL.Append_method(11)
DLL.Append_method(22)
DLL.Append_method(33)
DLL.Display()
DLL.DeleteLastNode()
DLL.Display()

