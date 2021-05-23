class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class listOperation:
    def __init__(self):
        self.head = None

    def traversList(self):
        curNode = self.head
        while True:
            print(curNode.data,end=' ')
            curNode = curNode.next
            if curNode.next == None:
                print(curNode.data)
                break
    @staticmethod
    def reverse(head):
        if head.next != None:
            listOperation.reverse(head.next)
        print(head.data,end= ' ')

    def reversList(self):
        curNode = self.head
        self.head = curNode.next
        curNode.next = None
        while True:
            curNodeNext = self.head.next
            self.head.next = curNode

            
    def printRevers(self):
        listOperation.reverse(self.head)


List = listOperation()
n1 = node(5)
n2 = node(6)
n3 = node(9)
n4 = node(10)

List.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
List.traversList()
List.printRevers()
