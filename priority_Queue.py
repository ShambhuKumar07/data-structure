import timeit
class priority_queue:
    def __init__(self):
        self.heap=[]

    def is_empty(self):
        return len(self.heap)==0
    
    def enqueue(self,element,priority):
        entry=(priority,element)

        self.heap.append(entry)
        self._heapify_up()

    def dequeue(self):
        if self.is_empty():
            return IndexError("Priority queue is empty")
        self._swap(0,len(self.heap)-1)

        property,element=self.heap.pop()
        self._heapify_down()
        return element
    
    def _heapify_up(self):
        index=len(self.heap)-1
        while index>0:
            parent_index=(index-1)//2
            if self.heap[index][0]<self.heap[parent_index][0]:
                self._swap(index,parent_index)
                index=parent_index

            else:
                break

    def _heapify_down(self):
        index=0
        while True:
            left_index=2*index+1
            right_index=2*index+1
            smallet_index=index

            if left_index<len(self.heap) and self.heap[left_index][0]<self.heap[smallet_index][0]:
                smallet_index=left_index
            if right_index<len(self.heap) and self.heap[right_index][0]<self.heap[smallet_index][0]:
                smallet_index=right_index
            
            if smallet_index!=index:
                self._swap(index,smallet_index)
                index=smallet_index
            else:
                break

    def _swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

    def Display(self):
        if self.is_empty():
            print("Queue is empty")

        else:
            print("Priority Queue ")
            for priority,element in self.heap:

                print(f"Priority:{ priority}, Element:{ element}")
                # print(timeit.timeit(stmt=priority))
                # print(timeit.timeit(stmt=element))


PQ=priority_queue()
PQ.enqueue(20,1)
PQ.enqueue(30,3)
PQ.enqueue(50,2)
PQ.Display()

