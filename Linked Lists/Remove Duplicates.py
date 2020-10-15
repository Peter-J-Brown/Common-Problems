class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next=self.head
        self.head = node

    def printl(self):
        current  = self.head
        while current:
            print(current.data)
            current= current.next

    def removeDups(self):
        current = second = self.head
        while current is not None:
            while second.next is not None:  # check second.next here rather than second
                if second.next.data == current.data:  # check second.next.data, not second.data
                    second.next = second.next.next  # cut second.next out of the list
                else:
                    second = second.next  # put this line in an else, to avoid skipping items
            current = second = current.next
#        l.printl()


llist = LinkedList()
llist.insert(15)
llist.insert(14)
llist.insert(16)
llist.insert(15)
llist.insert(15)
llist.insert(14)
llist.insert(18)
llist.insert(159)
llist.insert(12)
llist.insert(10)
llist.insert(15)
llist.insert(14)

llist.printl()

print("===============")

llist.removeDups()
llist.printl()