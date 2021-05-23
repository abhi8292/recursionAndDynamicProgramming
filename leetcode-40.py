class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        self.ans = []
        candidates.sort()
        def dfs(candidates, target, cur, pos):

            if target == 0:
                self.ans.append(cur.copy())
                return
            if target < 0:
                return

            for i in range(pos, len(candidates)):
                if i == pos or candidates[i] != candidates[i-1]:
                    cur.append(candidates[i])
                    dfs(candidates, target - candidates[i], cur, i + 1)
                    # pos = pos + 1
                    cur.pop()
                # target
            # pass

        dfs(candidates, target, [], 0)
        print(self.ans)

inp = [10,1,2,7,6,1,5]
target = 8

Solution().combinationSum2(inp,target)