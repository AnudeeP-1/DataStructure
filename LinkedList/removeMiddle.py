from asyncio.windows_events import NULL


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

    def removeMiddle(self):
        count=1
        node = self.head
        while node!=None:
            count = count+1
            node = node.next

        if count==0 or count==1:
            print("None")
        else:
            middle = int(count/2)

        count=0
        node = self.head
        while node!=None:
            if count!=middle:
                print(node.data)
                node = node.next
            else:
                node = node.next
            count = count+1
            

lList = LinkedList()
for i in range(4,0,-1):
    lList.push_front(i)

lList.printList()
lList.removeMiddle()