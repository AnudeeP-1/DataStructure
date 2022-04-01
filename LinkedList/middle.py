class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node

    def printList(self):
        node = self.head
        while node:
            print(str(node.data) + "->", end="")
            node = node.next
        print("NULL")

    def printMiddle(self):
        one_step_ptr = self.head
        two_step_ptr = self.head

        while two_step_ptr.next!=None:
            two_step_ptr = two_step_ptr.next
            if two_step_ptr.next != None:
                two_step_ptr = two_step_ptr.next
                one_step_ptr = one_step_ptr.next
        if(count%2==0):
            print(one_step_ptr.data, one_step_ptr.next.data)
        else:
            print(one_step_ptr.data)

obj = LinkedList()
count=0
for i in range(1,7):
    count = count+1
    print(i, end=" ")
    obj.push_front(i)

print("\n")
obj.printList()
obj.printMiddle()