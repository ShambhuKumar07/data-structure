class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=self.rear=None

    def isEmpty(self):
        return self.front==None
    
    def EnQueue(self,item):
        temp=Node(item)

        if self.rear==None:
            self.front=self.rear=temp

            return 
        self.rear.next=temp
        self.rear=temp

    def DnQueue(self):
        if self.isEmpty():
            return
        temp=self.front
        self.front=temp.next

        if(self.front==None):
            self.rear=None

    def Display(self):
        if self.isEmpty():
            print("Linked List is Empty")
        else:
            temp=self.front
            print("Front",self.front.data,end="")
            print("\n")
            while temp is not None:
                print(temp.data,"<--",end="")

                temp=temp.next
            print("\nRear",self.rear.data,end="")
            print()
Q=Queue()
Q.EnQueue(10)
Q.EnQueue(20)
Q.EnQueue(30)
Q.EnQueue(40)
Q.DnQueue()
Q.Display()