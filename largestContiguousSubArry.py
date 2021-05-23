li = [-2,-3,4,-1,-2,1,5,4,-3]

def findMax(li,i,sum):
    if i == len(li)-1:
        return sum

    return max(findMax(li,i+1,sum+li[i]),findMax(li,i+1,0))

print(findMax(li,0,0))


def FindMaxON(li):
    maxTillHere = 0
    maxSoFar =0

    for i in range(0,len(li)):
        maxTillHere = maxTillHere+li[i]
        if maxTillHere <0:
            maxTillHere = 0
        if maxTillHere > maxSoFar:
            maxSoFar = maxTillHere
    print(maxSoFar)

FindMaxON(li)