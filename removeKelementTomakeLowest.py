
def findLowest(inp,k):
    stk =[inp[0]]
    i = 1
    while k > 0 and i < len(inp):

        ele = stk.pop()
        while ele > inp[i] and k >0:
            if len(stk) > 0:
                ele = stk.pop()
                k -= 1
            else:
                k -= 1
                break

        if ele < inp[i]:
            stk.append(ele)

        if inp[i] == '0' and len(stk) == 0:
            # i += 1
            # continue
            while i < len(inp) and len(stk) == 0:
                if inp[i] != '0':
                    stk.append(inp[i])
                    i += 1
                    break
                else:
                    i += 1
        else:
            stk.append(inp[i])
            i += 1
    for j in range(i,len(inp)):
        stk.append(inp[j])

    while k >0:
        stk.pop()
        k -= 1
    print(stk)
    print(k)




inp = '12345678'
k = 4

findLowest(inp,k)