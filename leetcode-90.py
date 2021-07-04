class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        l = len(nums)
        nums.sort()
        ans = []

        def dfs(cur, pos):

            ans.append(cur.copy())

            if pos == l: return

            for i in range(pos, l):
                if i > pos and nums[i] == nums[i - 1]: continue
                cur.append(nums[i])
                dfs(cur, i + 1)
                cur.pop()

        dfs([], 0)
        return ans

inp = [1,1,2]

ans = Solution().subsetsWithDup(inp)
print(ans)