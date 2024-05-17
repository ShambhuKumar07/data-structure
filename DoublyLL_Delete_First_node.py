class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def Append_Method(self,data):
        New_Node=Node(data)
        if self.head is None:
            self.head=New_Node
        else:

            temp=self.head
            while temp.next is not None:
                temp=temp.next

            temp.next=New_Node
            New_Node.prev=temp
    def delete_first_node(self):
        if self.head is not None:
            Second_Node=self.head.next

            if Second_Node:
                Second_Node.prev=None
            self.head=Second_Node

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
DLL.Append_Method(5)
# DLL.Append_Method(10)
# DLL.Append_Method(15)
# DLL.Append_Method(20)
# DLL.Append_Method(25)
DLL.Display()
DLL.delete_first_node()
DLL.Display()