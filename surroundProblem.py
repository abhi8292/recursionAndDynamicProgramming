class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.memo={}
        def changeVal(board, i, j,memo):
            key =str(i)+','+str(j)
            print(i,j)
            print(memo)
            if key in self.memo.keys():
                return self.memo[key]
            if ((i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and board[i][j] == 'O'):
                self.memo[key] = False
                return False
            if board[i][j] == 'X':
                self.memo[key] = True
                return True
            if board[i][j] == 'O':
                board[i][j] = 'X'
                ans1 = changeVal(board, i + 1, j,self.memo)
                ans2 = changeVal(board, i - 1, j,self.memo)
                ans3 = changeVal(board, i,j + 1,self.memo)
                ans4 = changeVal(board, i, j - 1,self.memo)

            ans = ans1 and ans2 and ans3 and ans4
            self.memo[key] = ans
            if ans == False:
                board[i][j] = 'O'
            return ans

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 'O':
                    changeVal(board, i, j,self.memo)

        return board

board=[["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]

print(Solution().solve(board))
