class Solution:
    def isSafe(self,x,y,n):
        curX = x - 1
        curY = y - 1
        while curX>= 0 and curY >= 0:
            if self.chessBrd[curX][curY] == "Q":
                return False
            curY -= 1
            curX -= 1
        curX = x - 1
        curY = y
        while curX >= 0 and curY >= 0:
            if self.chessBrd[curX][curY] == "Q":
                return False
            curX -= 1
        curX = x - 1
        curY = y + 1
        while curX >= 0 and curY < n:
            if self.chessBrd[curX][curY] == "Q":
                return False
            curX -= 1
            curY += 1
        return True

    def solveNQueens(self, n: int) -> list[list[str]]:
        if n == 1:
            return [["Q"]]
        if n == 2 or n == 3:
            return []
        self.chessBrd = []
        row = ['.']* n
        for i in range(0,n):
            self.chessBrd.append(row.copy())

        self.ans = []

        def prePNqueen(ches, ind,n):
            if ind == n:
                self.ans.append(ches.copy())
                return

            for i in range(0,n):
                if self.isSafe(ind,i,n):
                    ches[ind][i] = 'Q'
                    prePNqueen(ches,ind+1,n)
                    ches[ind][i] = '.'



        prePNqueen(self.chessBrd.copy(),0,n)
        print(self.ans)





inp = 1
print(Solution().solveNQueens(inp))