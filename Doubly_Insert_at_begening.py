class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def Add_at_Begening(self,element):
        New_Node=Node(element)
        if self.head is not None:
            
            New_Node.next=self.head
            self.head.prev=New_Node

        self.head=New_Node

    def Display(self):
        if self.head is None:
            print("Linked List is Empty")

        else:
            Temp=self.head
            while Temp:
                print(Temp.data,"<->",end="")
                Temp=Temp.next
            print()

DLL=DoublyLinkedList()
DLL.Add_at_Begening(30)
DLL.Add_at_Begening(300)
DLL.Add_at_Begening(3000)
DLL.Add_at_Begening(30000)
DLL.Display()
