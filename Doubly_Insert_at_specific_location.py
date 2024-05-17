class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def Insertion_Operation(self,position,data):
        New_Node=Node(data)
        if position==1:
            New_Node.next=self.head
            if self.head:
                self.head.prev=New_Node
            self.head=New_Node

        else:
            current=self.head
            count=1
            while current and count<position-1:
                current=current.next
                count +=1

            if current:
                New_Node.next=current.next
                New_Node.prev=current
                if current.next:
                    current.next.prev=New_Node

                current.next=New_Node
            else:
                # Handle the case where current is None (end of the list)
                print("Position is out of range")

    def Display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            Temp1=self.head
            while Temp1:
                print(Temp1.data,"<=>",end="")
                Temp1=Temp1.next
            print()

DLL=DoublyLinkedList()
DLL.Insertion_Operation(1,111)
DLL.Insertion_Operation(1,222)
DLL.Insertion_Operation(3,333)
DLL.Insertion_Operation(4,444)
DLL.Insertion_Operation(5,555)
DLL.Insertion_Operation(6,666)
DLL.Insertion_Operation(7,777)
DLL.Insertion_Operation(8,888)
DLL.Insertion_Operation(9,999)
DLL.Insertion_Operation(9,  91199)

DLL.Display()

