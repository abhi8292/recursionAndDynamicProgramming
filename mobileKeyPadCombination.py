class Solution:
    def letterCombinations(self, digits: str):
        self.ans = []
        if len(digits) == 0:
            return self.ans
        self.bkt(0,digits,"")
        print(self.ans)
    def bkt(self,x,num,solution):
        keyMap = [None,None,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        for i in keyMap[int(num[x])]:
            solution += i
            if x < len(num)-1:
                self.bkt(x+1,num,solution)
            else:
                self.ans.append(solution)
            solution = solution[:x]

Solution().letterCombinations("2346")



