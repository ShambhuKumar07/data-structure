List=[]
size=int(input("Please Enter Size of the List :"))

for i in range(size):
    num=int(input("Please Enter incresing/decresing order of Number:"))
    List.append(num)

print("Original List:",List)

###### implement Binary Search

beg=0
end=len(List)-1
Item=40
Found=False
while beg<=end:
    mid=(beg+end)//2
    if List[mid]==Item:
        print("Item is Found")
        Found=True
        break
    elif List[mid]<Item:
        beg=mid+1
    else:
        end=mid-1

if not Found:
    print("Item is not found")



