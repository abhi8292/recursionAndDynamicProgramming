class Solution:
    def generateParenthesis(self, n: int):

        ans = []

        def dfs(cur, start, end):

            if start == n and end == n:
                ans.append(cur)
                return

            if start < n:
                dfs(cur + '(', start + 1, end)
            if end < start:
                dfs(cur + ')', start, end + 1)

        dfs("", 0, 0)
        return ans

print(Solution().generateParenthesis(2))