class Solution:
    sol = [""]
    def letterCombinations(self, digits):
        self.sol.clear()
        self.sol = [""]
        if digits == "":
            return ([])
        self.bkt(0,digits,"")
        self.sol.remove(self.sol[0])
        return self.sol
    def bkt(self,x,number,solution):
        letter_list = [None,None,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        for i in letter_list[int(number[x])]:
            solution += i
            if x < len(number)-1:
                self.bkt(x+1,number,solution)
            else:
                self.sol.append(solution)
                solution = solution[:x]
            solution = solution[:x]


print(Solution().letterCombinations("273"))