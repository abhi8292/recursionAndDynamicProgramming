class linkNode:

    def __init__(self,data):
        self.data = data
        self.next = None


def traverseLink(root):

    cur = root
    while cur:
        print(cur.data , end=" ")
        cur = cur.next

def rotateKPlace(root,k):
    cur = root
    count = 0
    while count < k-1 :
        cur = cur.next
        k -= 1
    # print(cur.data)
    head = cur.next
    cur.next = None
    newcur = head
    while newcur.next:
        newcur = newcur.next
    newcur.next = root
    return head





l1 = linkNode(2)
l2 = linkNode(3)
l3 = linkNode(5)
l4 = linkNode(4)
l5 = linkNode(9)
l6 = linkNode(8)
l7 = linkNode(7)
l8 = linkNode(6)


l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
root = l1

traverseLink(root)
hed = rotateKPlace(root,3)
print()
traverseLink(hed)
