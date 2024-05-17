# def S_push(item):
#     stk.append(item)
#     print(stk)

# stk=[22,33,4,5]

# S_push(999)
# S_push(999)
# S_push(999)
# S_push(999)

###################### using class   ##############


class STACK:
    def __init__(self):
        self.item=[]

        self.top=0

    def push(self,item):
        self.item.append(item)

        self.top=self.top-1
    
    def Display(self):
        if self.item==[]:
            print("stack is empty")

        else:
            print(self.item)

STK=STACK()
STK.push(100)
STK.push(200)
STK.push(300)
STK.push(400)
STK.Display()