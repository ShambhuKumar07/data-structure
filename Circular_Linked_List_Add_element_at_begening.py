
class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class CircularLinkedList:
    def __init__(self):
        self.head=None

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
    # def Append(self,data):
    #     New_Node=Node(data)
    #     if self.head is None:
    #         self.head=New_Node
    #     else:
    #         temp=self.head
    #         while temp.link !=self.head:
    #             temp=temp.link
    #         temp.link=New_Node

    #         New_Node.link=self.head


    def insert_at_beginning(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.link = self.head 
        else:
            current = self.head
            while current.link != self.head:
                current = current.link
            current.link = new_node
            new_node.link = self.head
            self.head = new_node

DLL=CircularLinkedList()
DLL.insert_at_beginning(200)
DLL.insert_at_beginning(200)
DLL.insert_at_beginning(200)
DLL.insert_at_beginning(200)
DLL.insert_at_beginning(200)
DLL.insert_at_beginning(200)
DLL.insert_at_beginning(200)

DLL.Display()









	 	 
