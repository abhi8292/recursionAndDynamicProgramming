def findPowerOFN(val,power):

    if power == 1:
        return val
    if power == 0:
        return 1
    if power %2 == 0:
        return findPowerOFN(val,power//2) * findPowerOFN(val,power//2)
    else:
        return findPowerOFN(val,power//2) * findPowerOFN(val,(power+1)//2)


print(findPowerOFN(5,8))