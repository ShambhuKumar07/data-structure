class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class Circular_Linked_List:
    def __init__(self):
        self.head=None
    
    def Append(self,item):
        New_Node=Node(item)
        if self.head is None:
            self.head=New_Node
            New_Node.link=self.head
        else:
            temp=self.head
            while temp.link!=self.head:
                temp=temp.link

            temp.link=New_Node
            New_Node.link=self.head

    def Display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            Temp=self.head
            while True:
                print(Temp.data)
                Temp=Temp.link

                if Temp==self.head:
                    break

            print()
CLL=Circular_Linked_List()
CLL.Append(12)
CLL.Append(13)
CLL.Append(14)
CLL.Append(15)
CLL.Display()