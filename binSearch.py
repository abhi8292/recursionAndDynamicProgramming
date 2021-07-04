def binSear(num,target):

    i = 0
    j = len(num)-1
    while i <= j:
        mid = (i+j)//2

        if num[mid] == target:
            return mid
        elif num[mid] < target:
            i = mid + 1
        else:
            j = mid -1
    return -1


inp = [2, 3, 4, 5, 6, 7, 32, 36, 43, 54, 56, 60, 76, 86, 435]


print(inp)
# nu = 43
print(binSear(inp,1))
