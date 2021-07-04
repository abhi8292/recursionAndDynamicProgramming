class Solution:
    def canCross(self, stones: list[int]) -> bool:

        des = stones[len(stones)-1]
        def canCros(cur,step):
            if cur not in stones or step == 0:
                return False
            if cur == des:
                return True
            return canCros(cur+step+1,step+1) or canCros(cur+step,step) or canCros(cur+step-1,step-1)
        print(canCros(1, 1))

inp = [0,1,3,5,6,8,12,19]

Solution().canCross(inp)