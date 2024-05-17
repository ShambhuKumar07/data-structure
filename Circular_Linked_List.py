class Node:
    def __init__(self,data):
        self.data=data
        self.link=None
    
class CircularSinglyLinkedList:
    def __init__(self):
        self.head=None

    def Append_Element_in_Circular_LL(self,data):
        New_Node=Node(data)
        if not self.head:
            self.head=New_Node
            self.head.link=self.head
        else:
            Temp=self.head

            while Temp.link !=self.head:
                Temp=Temp.link

            Temp.link=New_Node
            New_Node.link=self.head

    def Display(self):
        if not self.head:
            print("Linked List is Empty")
            return
        
        
        current=self.head
        while True:
            print(current.data)
            current=current.link
            if current == self.head:
                break
            print()

CLL=CircularSinglyLinkedList()
# print(id(CLL))
# print(type(CLL))
# print(id(CLL))
CLL.Append_Element_in_Circular_LL(33)
CLL.Append_Element_in_Circular_LL(34)
CLL.Append_Element_in_Circular_LL(35)
CLL.Append_Element_in_Circular_LL(36)
CLL.Append_Element_in_Circular_LL(37)
CLL.Display()