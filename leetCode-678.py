
class Solution:
    def checkValidString(self, s: str) -> bool:
        starStack = []
        paraStack = []
        size = len(s)
        for i in range(size):
            if s[i] == '*':
                starStack.append(i)
            else:
                if s[i] == '(':
                    paraStack.append(i)
                elif s[i] == ')':
                    if len(paraStack) > 0:
                        paraStack.pop()
                    else:
                        paraStack.append(i)
        print(starStack)
        print(paraStack)
        if len(paraStack) == 0:
            print(True)
            return

        while len(paraStack) > 0:
            ind = paraStack.pop()
            if s[ind] == ')':
                sInd = starStack.pop()
                






# inp = '(*)'
inp = '*(()*))'
Solution().checkValidString(inp)