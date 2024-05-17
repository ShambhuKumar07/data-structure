
def enqueue():
    n=int(input("Please enter the element to be inserted into queue:"))
    queue.append(n)

def dequeue():
    if len(queue)==0:
        print("Queue is empty")
        print()
    else:
        print(queue[0],"is the deleted from the Queue")

        del queue[0]

        print()
def Display():
    if len(queue)==0:
        print("Queue is empty")
 
    else:
        print("Elements of the Queue are")

        for i in queue:
            print(i," ",end="")

        print("\nFront element of the Queue",queue[0])
        print("Rear element of the Queue",queue[-1])

queue=list()

while(1):
    print("Enter the option from below:\n1-Enqueue Operation \n2-Dequeue Operation\n3-Display\n4-Exit")

    option=int(input("Please Enter Option 1 to 4:"))


    if option==1:
        print("Enqueue Operation")
        enqueue()
    elif option==2:
        print("Dequeue Operation")
        dequeue()
    elif option==3:
        print("Display Operation")
        Display()

    else:
        break
