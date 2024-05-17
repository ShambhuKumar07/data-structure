class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class CircularLinkedList:
    def __init__(self):
        self.head=None

    def Append(self,item):
        New_Node=Node(item)
        if not self.head:
            self.head=New_Node
            self.head.link=self.head

        else:
            current =self.head
            while current.link != self.head:
                current=current.link

            current.link=New_Node
            New_Node.link=self.head

    def delete_first(self):
        if not self.head:
            print("Linked List is Empty")
        else:
            temp=self.head
            while temp.link !=self.head:
                temp=temp.link

            temp.link=self.head.link
            self.head=self.head.link

    def Display(self):
        if not self.head:
            print("Linked List is Empty")
        else:
            temp=self.head
            while True:
                print(temp.data,"<->",end="")
                temp=temp.link
                if temp==self.head:
                    break
            print()
CLL=CircularLinkedList()
CLL.Append(10)
CLL.Append(20)
CLL.Append(30)
CLL.Append(40)
print("Original Linked List")
CLL.Display()

CLL.delete_first()
print("Linked List after deleting the first node")
CLL.Display()
