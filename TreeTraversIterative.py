class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def InOrder(root):
    cur = root
    stk =[]
    while True:
        if cur is not None:
            stk.append(cur)
            cur = cur.left
        elif(stk):
            cur = stk.pop()
            print(cur.val,end=" ")
            cur = cur.right
        else:
            break


def inorderIter(root):
    stk = []
    cur = root
    while True:
        if cur is not None:
            stk.append(cur)
            cur = cur.left
        elif stk:
            cur = stk.pop()
            print(cur.val,end= " ")
            cur = cur.right
        else:
            break


# Wrong Program
def postOrder(root):
    stk = []
    cur = root
    while True:
        if cur is not None:
            stk.append(cur)
            cur = cur.left
        elif stk:
            cur = stk.pop()
            temp = cur
            cur = cur.right
            print(temp.val,end=" ")
        else:
            break

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# InOrder(root)
# print()
# inorderIter(root)
# print()
postOrder(root)
