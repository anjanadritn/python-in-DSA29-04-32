# linked list
class LinkedList:

    def __init__(self):
        self.head = None   # initialize head

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def ins_begg(self, data):
        nn = LinkedList.Node(data)
        nn.next = self.head
        self.head = nn

    def traverse(self):
        c = self.head
        while c:
            print(c.data)
            c = c.next


# usage (outside class)
l1 = LinkedList()
l1.ins_begg(93)
l1.ins_begg(83)
l1.ins_begg(33)
l1.ins_begg(73)

l1.traverse()