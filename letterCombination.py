class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        self.dic={'2':"abc",'3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.ans = []

        def combinationOfLetter(digit,cur,size):

            if size == len(digit):
                self.ans.append(cur)
                return
            target = self.dic[digits[size]]
            for i in target:
                combinationOfLetter(digit,cur+i,size+1)


        combinationOfLetter(digits,'',0)
        return self.ans

print(Solution().letterCombinations('23'))