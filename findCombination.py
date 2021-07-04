class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        self.ans = []

        def findCombination(n, k, cur, size, ind):

            if k == size:
                self.ans.append(cur.copy())
                return
            for i in range(ind, n+1):
                findCombination(n, k, cur + [i], size + 1, i+1)

        findCombination(n, k, [], 0, 1)

        return self.ans

print(Solution().combine(4,2))