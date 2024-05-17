class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def Traversal(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp=self.head
            while temp.li is not None:
                print(temp.data,"->",end="")
                temp=temp.link
            print()

obj=SinglyLinkedList()
obj.head=Node(11)  ## Assign FIrst Node to Head    ## create Firs Node
print(obj.head)
d2=Node(22)        ## create Second Node
d3=Node(33)        ## create Third Node
d4=Node(44)        ## create FOurth Node
obj.head.link=d2 # Link first Node to second Node
d2.link=d3
d3.link=d4
T=obj.Traversal()
# print("->",T,end="")
