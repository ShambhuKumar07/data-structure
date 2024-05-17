class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class CircularLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_specific_postion(self,data,position):
        New_Node=Node(data)
        if not self.head:
            New_Node.link=New_Node
            self.head=New_Node
        else:
            current=self.head
            count=1
            while count<position-1:
                current=current.link
                count +=1

            New_Node.link=current.link
            current.link=New_Node

    def Display(self):
        if not self.head:
            return
        
        temp=self.head
        while True:
            print(temp.data,"<->",end="")
            temp=temp.link

            if temp==self.head:
                break
        print()
CLL=CircularLinkedList()
CLL.insert_at_specific_postion(10,1)
CLL.insert_at_specific_postion(10,2)
CLL.insert_at_specific_postion(10,3)
CLL.insert_at_specific_postion(10,4)
CLL.insert_at_specific_postion(10,5)
CLL.insert_at_specific_postion(10,6)
CLL.insert_at_specific_postion(10,7)
CLL.insert_at_specific_postion(1000,3)
CLL.Display()