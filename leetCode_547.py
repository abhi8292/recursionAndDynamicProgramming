class Solution:
    def findCircleNum(self, isConnected) -> int:

        adjList = {}
        size = len(isConnected)
        for i in range(0, size):
            adjList[i] = []
            for j in range(0, size):

                if isConnected[i][j] == 1:
                    if i == j:
                        continue
                    adjList[i].append(j)

        def dfs(src,mat):

            # isConnected[src][src] = 0
            visited = [src]

            while visited:
                source = visited.pop(0)
                isConnected[source][source] = 0
                if source in adjList.keys():
                    visited = visited + adjList[source]
                    del adjList[source]
                if len(visited) > 0:
                    for k in visited:
                        isConnected[source][k] = 0

        count = 0

        for i in range(0, size):
            for j in range(0, size):
                if isConnected[i][j] == 1:
                    dfs(i,isConnected)
                    count += 1

        print(adjList)

inp = [[1,1,0],[1,1,0],[0,0,1]]

Solution().findCircleNum(inp)