class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def APPEND(self,element):
        new_node=Node(element)
        if not self.head:
            self.head=new_node
        else:
            temp=self.head
            while temp.link:
                temp=temp.link
            temp.link=new_node


    def LinearSearch(self,item):
        current=self.head
        while current:
            if current.data==item:
                return True
            current=current.link

        return False
    
SLL=SinglyLinkedList()
SLL.APPEND(30)
SLL.APPEND(40)
SLL.APPEND(50)
SLL.APPEND(60)
SLL.APPEND(70)


if SLL.LinearSearch(40):
    print("Item is found")
else:
    print("Item is not found")

 