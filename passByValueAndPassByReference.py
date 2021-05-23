a = [1,2,3]


def setA(myList):
    myList = [4,5,6]
    return myList

def changeA(a):
    a = [4,5,6]
    # return a
print(a)
a2 = setA(a)
print(a)
print(a2)
a3 = changeA(a)
print(a)
print(a3)