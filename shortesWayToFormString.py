def shotestWayToFormString(src,target):

    remain = target
    count = 0
    while len(remain) > 0:
        i = 0
        j = 0
        temp =[]
        while i <len(src) and j < len(remain):
            if src[i] == remain[j]:
                temp.append(remain[j])
                j += 1
            i += 1

        if len(temp) == 0:
            return -1
        remain = remain[len(temp):]
        count += 1
    print(count)


src = 'abc'
target = 'abcdbc'
print(shotestWayToFormString(src,target))