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
        row = "."*n
        for i in range(0,n):
            self.chessBrd.append(row)

        self.ans = []

        def prePNqueen(ches, ind,n):
            if ind == n:
                self.ans.append(ches.copy())
                return

            for i in range(0,n):
                if self.isSafe(ind,i,n):
                    li = list(ches[ind])
                    li[i] = 'Q'
                    ches[ind] = "".join(li)
                    prePNqueen(ches,ind+1,n)
                    li[i] = '.'
                    ches[ind] = "".join(li)



        prePNqueen(self.chessBrd,0,n)
        print(self.ans)
        # print(self.chessBrd)





inp = 4
print(Solution().solveNQueens(inp))