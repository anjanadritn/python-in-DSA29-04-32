class LinkedList:

    def __init__(self):
        self.head = None   

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

            def remove_nth(self,n):
                l=0
                c=self.head
                while c:
                    l+=1
                    c=c.next
                    if l==n:
                        return self.head.data
                    c1=self.head   #90
                    for _ in range(l-n-1): #loop runs 9-4-1=4 times
                        c1=c1.next         #67,44,33,21
                        c1.next=c1.next.next
                        return self.head
