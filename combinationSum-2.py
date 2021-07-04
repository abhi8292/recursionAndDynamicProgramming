class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        if candidates is None or len(candidates) == 0:
            return []
        if target == 0 or target == None:
            return []
        self.ans = []
        candidates.sort()
        def dfs(candidates,pos,cur,target):

            if target == 0:
                self.ans.append(cur.copy())
                return
            if target < 0:
                return

            for i in range(pos,len(candidates)):
                if candidates[i] != candidates[i-1] or i == pos:
                    dfs(candidates,i+1,cur+[candidates[i]],target-candidates[i])


        dfs(candidates,0,[],target)
        print(self.ans)


inp = [10,1,2,7,6,1,5]
target = 8
Solution().combinationSum2(inp,target)