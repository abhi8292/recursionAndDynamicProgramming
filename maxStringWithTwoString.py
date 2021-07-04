
def maxStringWith2String(string):

    i = 0
    j = 1
    dic = {}
    dic[string[i]] = 1
    flag = True
    maxLen = 1
    temp = 1
    while j < len(string) and i < len(string):
        if flag:
            if string[j] in dic.keys():
                dic[string[j]] = dic[string[j]] + 1
            else:
                dic[string[j]] = 1
            if len(dic) <= 2:
                temp += 1
                j += 1
            else:
                del dic[string[j]]
                dic[string[i]] = dic[string[i]] - 1
                if dic[string[i]] == 0:
                    del dic[string[i]]
                i += 1
                temp -= 1

        maxLen = max(maxLen,temp)
    print(maxLen)



# inp = 'xyxxxyzxzzzzzz'
inp = [3,3,3,1,2,1,1,2,3,3,4]
maxStringWith2String(inp)