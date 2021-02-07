'''
Given Two string, write a function that return the longest common substring.

subString('ABAB','BABA') => ABA

'''
a = 'ABAB'
b = 'BABA'
def findLargestSubstring(a,b):
    ans = ''
    print(a , b)
    maxLen = 0
    if not a or not b:
        return ''
    grid = [0]*(len(a)+1)
    finalGrid = [[0]*(len(b)+1) for g in grid]
    # print(finalGrid)
    for i in range(len(a)):
        temp =''
        for j in range(len(b)):
            # print(i,j)
            if a[i] == b[j]:
                finalGrid[i+1][j+1] = finalGrid[i][j] + 1
                if maxLen < finalGrid[i+1][j+1]:
                    maxLen = finalGrid[i+1][j+1]
    print(maxLen)
    # print(finalGrid)
    for i in finalGrid:
        print(i)
    for i in range(0,maxLen):
        print(a[i],end='')

findLargestSubstring(a,b)
# for i in grid:
#     print([0] *len(b))
# print(grid)