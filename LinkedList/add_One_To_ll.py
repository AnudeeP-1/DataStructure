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

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

lList = LinkedList()
# value =(09221)
# l=[]
# while value!=0:
#     rem = int(value%10)
#     l.append(rem)
#     value = int(value/10)
lList.push_front(9)
lList.push_front(2)
lList.push_front(2)
lList.push_front(1)
lList.push_front(0)
lList.reverse()

add=1
carry=0
node = lList.head
node.data += 1
while node!=None:
    if node.data>9:
        carry=1
        node.data=0
    else:
        if carry==1:
            node.data = node.data+carry
            carry=0
    node = node.next
    
lList.reverse()
lList.printList()