
def findNextGreaterElement(inp):
    # stk = [0] * len(inp)
    stk = [[inp[0],0]]
    ans = [0] * len(inp)
    for i in range(1,len(inp)):

        if len(stk) >0:
            ele = stk.pop()

            while ele[0] < inp[i]:

                ans[ele[1]] = inp[i]
                if len(stk) == 0:
                    break
                else:
                    ele = stk.pop()
            if ele[0] >= inp[i]:
                stk.append(ele)
        stk.append([inp[i],i])
    print(ans)


inp = [11,3,7,6,11,12]
findNextGreaterElement(inp)