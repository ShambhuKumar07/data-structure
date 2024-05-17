class STACK:
    def __init__(self):
        self.item=[]

        self.top=0

    def s_push(self,item):
        self.item.append(item)

        self.top -=1

    def s_pop(self):
        self.item.pop()
        self.top -=1

    def Display(self):
        if self.item==[]:
            print("Stack is empty")
        else:
            print(self.item)

STK=STACK()
STK.s_push(10)
STK.s_push(20)
STK.s_push(30)
STK.s_push(40)
STK.s_push(50)
STK.s_push(60)
STK.s_push(70)
STK.s_pop()
STK.Display()