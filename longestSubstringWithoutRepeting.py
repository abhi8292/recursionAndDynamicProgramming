
def longestSubstrinWithoutDuplicate(string):
    dicChar={}
    for i in string:
        if i not in dicChar.keys():
            dicChar[i] = 0
    print(dicChar)
    size = len(string)
    i = 0
    j = 1
    count = 1
    temp = 1
    for i in range(0,size):
        while j < size:
            if dicChar[string[j]] == 0:
                dicChar[string[j]] += 1
                j += 1
                temp += 1
            else:
                dicChar[string[i]] = 0
                count = max(temp,count)
                temp -= 1
                break
    print(count)


inp = ['a','a','r','e','x','r','z','x']
longestSubstrinWithoutDuplicate(inp)