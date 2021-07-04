class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # dir = [[0,1],[0,-1],[-1,0],[1,0]]
        dirX = [0, 0, -1, 1]
        dirY = [1, -1, 0, 0]
        self.visited = {}

        def dfs(x, y, way):
            key = str(x) + ',' + str(y)
            if x < 0 or y < 0 or x > len(matrix) - 1 or y > len(matrix[0]) - 1:
                return
            if matrix[x][y] > 0:
                self.visited[key] = 0
                matrix[x][y] = 0
            dfs(x + dirX[way], y + dirY[way], way)
            return

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                key = str(i) + ',' + str(j)
                if key in self.visited.keys():
                    continue

                if matrix[i][j] == 0:
                    dfs(i, j, 0)
                    dfs(i, j, 1)
                    dfs(i, j, 2)
                    dfs(i, j, 3)


inp = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(inp)
print(inp)