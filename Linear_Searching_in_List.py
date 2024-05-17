List=[]
size=int(input("Please Enter The Size of List :"))
for i in range(size):
    num=int(input("Please Enter Number:"))
    List.append(num)

print("Original List =",List)

k=0
found=False
item=10
while k<=len(List)-1:
    if item==List[k]:
        found=True
        break
    k=k+1

if found is True:
    print("Item is Founded ")

else:
    print("Item is not found")