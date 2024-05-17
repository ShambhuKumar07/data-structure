List=[]
Size=int(input("Please Enter Size of List :"))
for i in range(Size):
    num=int(input("Please Enter Number :"))
    List.append(num)

print("Original List is :",List)

del(List[0])

print("After deleting first item",List)