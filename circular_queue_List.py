class CircularQueue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=[None]*capacity
        self.front=self.rear=-1

    def is_empty(self):
        return self.front==-1
    
    def is_full(self):
        return (self.rear+1)%self.capacity==self.front
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty ")
        else:
            item=self.queue[self.front]
            if self.front==self.rear:
                self.front=self.rear=-1
            else:
                self.front=(self.front+1)%self.capacity

            print(f"Dequeued:{item}")
            return item
    def enqueue(self,item):
        if self.is_full():
            print("Queue is Full,cannot enqueue")

        else:
            if self.is_empty():
                self.front=self.rear=0
            else:
                self.rear=(self.rear+1)%self.capacity

            self.queue[self.rear]=item
            print(f"Enqueued:{item}")
    def display(self):
        if self.is_empty():
            print("Queue is empty ")
        else:
            print("Queue element:",end="")

            i=self.front
            while True:
                print(self.queue[i],"<-->",end="")
                if i==self.rear:
                    break

                i=(i+1)%self.capacity

            print()

    def peak(self):
        if self.is_empty():
            print("Queue is empty, Nothing to peak")
            return None
        else:
            return self.queue[self.front]



CQ=CircularQueue(5)
CQ.enqueue(110)
CQ.enqueue(10)
CQ.enqueue(10)
CQ.enqueue(10)
CQ.enqueue(100)
# CQ.enqueue(10)
print("The peak value is:",CQ.peak())
CQ.display()
