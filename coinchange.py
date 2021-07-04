class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        self.ans = []
        self.minLen=amount+1
        def option(coins, target, cur):

            if target < 0:
                return 0
            if target == 0:
                self.ans.append(cur.copy())
                self.minLen = min(len(cur),self.minLen)
                return
            for i in coins:
                cur.append(i)
                option(coins,target-i,cur)
                cur.pop()
        option(coins,amount,[])
        if self.minLen == amount+1:
            return -1
        else:
            return self.minLen



print(Solution().coinChange([1,2,3,4],100))