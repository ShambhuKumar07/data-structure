def partition(List,low,high):
    pivot=List[high]

    i=low-1

    for j in range(low,high):
        if List[j]<=pivot:
            i=i+1

            List[i],List[j]=List[j],List[i]
    List[i+1],List[high]=List[high],List[i+1]

    return i+1


def quicksort(List,low,high):
    if low<high:

        pi=partition(List,low,high)

        quicksort(List,low,pi-1)
        quicksort(List,pi+1,high)


L=[22,11,88,66,55,77,33,44]

size=len(L)

low=0

print("Unsorted List")
print(L)

quicksort(L,low,size-1)
print("Sorted List in accending order")
print(L)