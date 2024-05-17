#python program for Quick Sort Algorithm
intArray = [4, 6, 3, 2, 1, 9, 7]
MAX = 7
def printline(count):
    for i in range(count - 1):
        print("=", end="")
    print("=")
def display():
    print("[", end="")
    for i in range(MAX):
        print(intArray[i], end=" ")
    print("]")
def swap(num1, num2):
    temp = intArray[num1]
    intArray[num1] = intArray[num2]
    intArray[num2] = temp
def partition(left, right, pivot):
    leftPointer = left
    rightPointer = right - 1
    while True:
        while leftPointer <= right and intArray[leftPointer] < pivot:
            leftPointer += 1
        while rightPointer >= left and intArray[rightPointer] > pivot:
            rightPointer -= 1
        if leftPointer >= rightPointer:
            break
        else:
            print(" item swapped :", intArray[leftPointer], ",",
                  intArray[rightPointer])
            swap(leftPointer, rightPointer)
    print(" pivot swapped :", intArray[leftPointer], ",", intArray[right])
    swap(
        leftPointer, right
    )  # Swapping the pivot with the leftPointer (which is now at the correct position)
    print("Updated Array: ", end="")
    display()
    return leftPointer
def quickSort(left, right):
    if right <= left:
        return
    else:
        pivot = intArray[right]
        partitionPoint = partition(left, right, pivot)
        quickSort(left, partitionPoint - 1)
        quickSort(partitionPoint + 1, right)
intArray = [4, 6, 3, 2, 1, 9, 7]
MAX = 7
print("Input Array: ", end="")
display()
printline(50)
quickSort(0, MAX - 1)
print("Output Array: ", end="")
display()
printline(50)