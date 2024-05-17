list=[1,2,3,4,5,6,7,8]
size=len(list)
index=0
for i in range(index,size-1):
    list[i]=list[i+1]
    
list.pop()
print(list)