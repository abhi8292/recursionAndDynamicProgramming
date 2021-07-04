
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:

        self.image = image
        self.visited = {}

        def dfs(x, y, newColor, cur, visited):

            key = str(x) + ',' + str(y)

            if key in visited.keys():
                return

            if x < 0 or y < 0 or x == len(self.image) or y == len(self.image[0]):
                return

            visited[key] = True
            if self.image[x][y] != cur:
                return
            self.image[x][y] = newColor

            dfs(x + 1, y, newColor, cur, visited)
            dfs(x - 1, y, newColor, cur, visited)
            dfs(x, y + 1, newColor, cur, visited)
            dfs(x, y - 1, newColor, cur, visited)

        dfs(sr, sc, newColor, self.image[sr][sc], self.visited)
        print(self.image)

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
Solution().floodFill(image,sr,sc,newColor)