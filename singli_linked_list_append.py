class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class SinglyLinkList:
    def __init__(self):
        self.head=None

    def Add_Element_AT_End(self,newdata):
        new_node=Node(newdata)
        if self.head is None:
            self.head=new_node
             
        else:
            Temp=self.head
            while Temp.link is not None:
                Temp=Temp.link
            # Temp.link=new_node
            Temp.link = new_node
    def Travesal(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            Temp1=self.head
            while Temp1 is not None:
                print(Temp1.data,"->",end="")
                Temp1=Temp1.link
            print()

obj=SinglyLinkList()
obj.head=Node(1111)
N2=Node(6666)
N3=Node(7777)
N4=Node(8888)
obj.head.link=N2 
N2.link=N3
N3.link=N4
obj.Add_Element_AT_End(22222)
obj.Travesal()