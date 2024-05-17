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
            Temp=self.head
            while Temp.link!=self.head:
                Temp=Temp.link

            Temp.link=New_Node
            New_Node.link=self.head

    def Delete_First(self):
        if not self.head:
            print("Linked List is Empty")

        else:
            Current=self.head
            while Current.link!=self.head:
                Current=Current.link

            Current.link=self.head.link
            self.head=self.head.link

    def Delete_Specific_Node(self,target_value):
        if not self.head:
            print("Linked List is Empty")

        elif self.head.data==target_value:
            self.Delete_First()

        else:
            temp=self.head
            Found=False

            while temp:
                if temp.link.data==target_value:
                    Found=True
                    break
                temp=temp.link

                if temp.link==self.head:
                    break


            if Found:
                temp.link=temp.link.link

            else:
                print("Node with data", target_value, "not found in the list.")

    def Display(self):
        if not self.head:
            print("Linked List is Empty")

        else:
            temp=self.head

            while True:
                print(temp.data,"<=>",end="")

                temp=temp.link
                if temp==self.head:
                    break
            print()
CLL=CircularLinkedList()
CLL.Append(10)
CLL.Append(20)
CLL.Append(30)
CLL.Append(40)
CLL.Append(50)
CLL.Append(60)
print("Original Linked List")
CLL.Display()
CLL.Delete_First()

CLL.Delete_Specific_Node(40)
print("After deleting the node")
CLL.Display()