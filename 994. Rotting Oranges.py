class Solution:
    '''
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    '''
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rotten=[]
        self.numOfDays = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))

        def minNumberOfDays(rotten,grid):

            while rotten:
                temp = []
                for i in rotten:
                    x = i[0]
                    y = i[1]
                    if x+1 < len(grid):
                        if grid[x+1][y] != 0 and grid[x+1][y] != 2:
                            grid[x+1][y] = 2
                            temp.append((x+1,y))
                    if x-1 >= 0:
                        if grid[x-1][y] != 0 and grid[x-1][y] != 2:
                            temp.append((x-1,y))
                            grid[x-1][y] = 2
                    if y+1 < len(grid[0]):
                        if grid[x][y+1] != 0 and grid[x][y+1] != 2:
                            temp.append((x,y+1))
                            grid[x][y+1] = 2
                    if y-1 >= 0:
                        if grid[x][y-1] != 0 and grid[x][y-1] != 2:
                            temp.append((x,y-1))
                            grid[x][y-1] = 2
                rotten = temp
                if len(temp) > 0:
                    self.numOfDays += 1

        minNumberOfDays(rotten,grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return self.numOfDays




inp = [[0,2]]
print(Solution().orangesRotting(inp))
inp = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(inp))
inp = [[2,1,1],[0,1,1],[1,0,1]]
print(Solution().orangesRotting(inp))