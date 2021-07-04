def generateTruthTable(n,cur,ans):

    option = [0,1]
    if len(cur) == n:
        print(cur)
        ans.append(cur.copy())
        return
    for opt in option:
        cur.append(opt)
        generateTruthTable(n,cur,ans)
        cur.pop()




n = 3

generateTruthTable(n,[],[])