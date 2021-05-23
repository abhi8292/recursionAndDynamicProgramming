class Solution:
    def allPathsSourceTarget(self, graph):
        ans = []

        def bfsGraph(src,path):

            if graph[src] == []:
                ans.append(path)
                return

            for i in graph[src]:
                bfsGraph(i,path+[i])

        bfsGraph(0,[0])
        print(ans)



inp = [[4,3,1],[3,2,4],[],[4],[]]
Solution().allPathsSourceTarget(inp)