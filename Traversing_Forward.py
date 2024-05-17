class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.link=None

class Doubly_Linked_List:
    def __init__(self):
        self.head=None

    def Append(self,element):
        New_Node=Node(element)
        if not self.head:
            self.head=New_Node
        else:
            current=self.head

            while current.link:
                current=current.link

            current.link=New_Node
            New_Node.prev=current

    def Forward_Travers(self):
        if self.head is None:
            print("Linked List is Empty")

        Temp=self.head
        while Temp is not None:
            print(Temp.data,"<=>",end="")
            Temp=Temp.link
        print()


    def Backward_Traversal(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            Temp1=self.head
            while Temp1 and Temp1.link:

                if(Temp1.data==10):
                    print("item is present")
                Temp1=Temp1.link
            while Temp1:
                print(Temp1.data,"<=>",end="")

                Temp1=Temp1.prev
            print()

DLL=Doubly_Linked_List()
DLL.Append(10)
DLL.Append(20)
DLL.Append(30)
DLL.Append(40)
DLL.Append(50)
# DLL.Forward_Travers()
DLL.Backward_Traversal()