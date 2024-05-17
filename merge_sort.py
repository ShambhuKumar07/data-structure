def merge_sort(list1):

    ####### devide list into sub list
    if len(list1)>1:
        mid=len(list1)//2
        left_list=list1[:mid]
        right_list=list1[mid:]
        merge_sort(left_list) ##calling the merge_sort function -- recursive
        merge_sort(right_list) ##calling the merge_sort function -- recursive

        ######## sort and store the left_list and right_list in list1
        i=j=k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i +=1
                k +=1
            else:
                list1[k]=right_list[j]
                j+=1
                k+=1

        ###### if any element present left list stor the element in list1
        while i<len(left_list):
            list1[k]=left_list[i]
            i+=1
            k+=1
        ###### if any element present right list stor the element in list1
        while j<len(right_list):
            list1[k]=right_list[j]
            j+=1
            k+=1


num=int(input("Please Enter Size of List :"))
#### using list comprehension
list1=[int(input("please enter element in the list :")) for x in range(num)]

# list1=[38, 27, 43, 3, 9, 82, 10]
merge_sort(list1)
print(list1)