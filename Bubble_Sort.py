List=[1,2,6,34,7,2,9,75,8,45,8,8]
size=len(List)

for i in range(size):
    # print(List[i])
    for j in range(size-1):
        if(List[j]>List[j+1]):

            temp=List[j]
            List[j]=List[j+1]
            List[j+1]=temp
print(List)