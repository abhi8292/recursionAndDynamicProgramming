class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        self.ans = 0

        def dfs(i, j, grid, cnt):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:

                return 0
            temp = 1
            grid[i][j] = 0
            temp += dfs(i + 1, j, grid, cnt + 1)
            temp += dfs(i - 1, j, grid, cnt + 1)
            temp += dfs(i, j + 1, grid, cnt + 1)
            temp += dfs(i, j - 1, grid, cnt + 1)
            return temp

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.ans = max(self.ans,dfs(i, j, grid, 1))

        return self.ans

# inp = [[1,1,0,0,0],
#        [1,1,0,0,0],
#        [0,0,0,1,1],
#        [0,0,0,1,1]]
inp = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(inp))
