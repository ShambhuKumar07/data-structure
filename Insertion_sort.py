L=[64, 34, 25, 12, 22, 11, 90]

size=len(L)

for i in range(1,size):
    # print(L[i])
    current_element=L[i]
    

    j=i-1
    while j>=0 and current_element<L[j]:
        L[j+1]=L[j]
        j -=1


    L[j+1]=current_element

print("Insertion sort is ",L)
