
def findLargestSquare(inp):
    dp =[]
    temp = [0] * (len(inp[0])+1)
    for i in range(0,len(inp)+1):
        dp.append(temp.copy())
    lar = 0
    for i in range(0,len(inp)):
        for j in range(0,len(inp[0])):
            if inp[i][j] == 1:
                dp[i+1][j+1] = 1 + min(dp[i][j+1],dp[i+1][j],dp[i][j])
                lar = max(lar,dp[i+1][j+1])

    print(lar)
    print(dp)

inp = [[0,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[1,1,1,1,1]]
findLargestSquare(inp)