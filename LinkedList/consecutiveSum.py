from operator import index, indexOf


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

    def traverse(self):
        prefixSum = 0
        node = self.head
        while node!=None:
            prefixSum = prefixSum+node.data
            key_value_dict[node.data] = prefixSum
            node = node.next    

        print(key_value_dict)


lList = LinkedList()
lList.push_front(-3)
lList.push_front(4)
lList.push_front(3)
lList.push_front(-6)
lList.push_front(6)

lList.printList()

key_value_dict = {}
key_value_dict[0] = 0
lList.traverse()

ke = list(key_value_dict.keys())
l = list(key_value_dict.values())
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if(i!=j):
            if l[i]==l[j]:
                for k in range(i+1,j+1):
                        ke[k] = -9999
for i in ke:
    if i!=-9999 and index(i)!=0:
        print(i)