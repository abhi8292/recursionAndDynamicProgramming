class link:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linkList():

    def traverse(self,head):
        cur = head
        while cur:

            print(cur.data," =>",end=" ")
            cur = cur.next
        print(" None")

    def reverse(self,head):
        self.newHead = None
        cur = head
        prev = None
        nex = None
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        self.newHead = prev

        print("after reversing")
        self.traverse(self.newHead)

    def reverse(self,head,k):
        cur = head
        prev = None
        nex = None
        count = 0

        while cur and count < k:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
            count += 1

        if cur is not None:
            head.next = self.reverse(cur,k)

        return prev


    def revList(self,head):

        cur = head
        prv = None
        nex = None

        while cur:
            nex = cur.next
            cur.next = prv
            prv = cur
            cur = nex

        return prv

    def revListK(self,head,k):

        cur = head
        prv = None
        count = 0
        while cur and count < k:
            nex = cur.next
            cur.next = prv
            prv = cur
            cur = nex
            count += 1

        if cur is not None:
            head.next = self.revListK(cur,k)

        return prv






















l1 = link(1)
l2 = link(2)
l3 = link(3)
l4 = link(4)
l5 = link(5)
l6 = link(6)
l7 = link(7)
l8 = link(8)
l9 = link(9)
head = l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
l8.next = l9

linkList().traverse(head)
# linkList().reverse(head)
# linkList().traverse(linkList().reverse(head,3))
# he = linkList().revList(head)
# linkList().traverse(he)
linkList().traverse(linkList().revListK(head,4))

