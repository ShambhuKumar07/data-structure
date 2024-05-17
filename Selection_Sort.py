List=[64, 25, 12, 22, 11]
size=len(List)
for i in range(size):

    my_index=i

    for j in range(i+1,size):
        if List[j]<List[my_index]:
            my_index=j  

        
        List[i],List[my_index]=List[my_index],List[i]

print("Selection SOrt :",List)