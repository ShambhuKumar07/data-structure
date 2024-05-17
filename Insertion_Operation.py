List=[1,3,4,5,6,4,5,7,3]

size=len(List)
index=3
for i in range(size-1,index,-1):
    List[i]=List[i-1]

List[index]=400
size=size+1
print(List)