# l=[1,2,1,4,6,4,5,9,88,66]

# item=88

# found=False

# size=len(l)

# for i in range(size):
#     if l[i]==item:
#         found=True
#         break


# if found:
#     print("Element is founded")

# else:
#     print("element is not found")


################ Using Recursion

def Linear_Search(List,size,item):
    if size==0:
        return False
    
    if size==1:
        return True
    
    
    else:
        remaining=Linear_Search(List[1:],size-1,item)

        return remaining
    

List=[11,2,33,2,55,6,7,8,4,9,3,6,7,999]
size=len(List)
Key=999

Found=Linear_Search(List,size,Key)
if Found:
    print("item is present")

else:
    print("Item is not present")

