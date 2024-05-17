class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def Append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.link:
                temp = temp.link
            temp.link = new_node

    def binary_search(self, target):
        left = None
        right = self.head

        while right:
            mid = self.get_middle(left, right)

            if mid.data == target:
                return mid
            elif mid.data < target:
                left = mid.link
            else:
                right = mid

        return None

    def get_middle(self, left, right):
        if not right:
            return None

        slow = left
        fast = left

        while fast != right and fast.link != right:
            slow = slow.link
            fast = fast.link.link

        return slow

    def Traversal(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "->", end="")
                temp = temp.link
            print()

SLL = SinglyLinkedList()
SLL.Append(10)
SLL.Append(20)
SLL.Append(30)
SLL.Append(40)
SLL.Append(50)
SLL.Append(60)

SLL.Traversal()
target = 50
result = SLL.binary_search(target)
if result:
    print(f"Found {target} in the list.")
else:
    print(f"{target} not found in the list.")

target = 200
result = SLL.binary_search(target)
if result:
    print(f"Found {target} in the list.")
else:
    print(f"{target} not found in the list.")
