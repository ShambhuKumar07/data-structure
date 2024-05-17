class Queue:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.queue=[]
        self.front=self.rear=-1

    def is_empty(self):
        return self.front==-1
    

    def is_full(self):
        return (self.rear+1) % self.maxsize==self.front
    
    def enqueue(self,element):
        if self.is_full():
            print("Queue is Full, Can not enqueue ")

        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear=(self.rear+1)%self.maxsize

            self.queue.append(element)

            print(f"Enqueue :{element}")

queue=Queue(5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)