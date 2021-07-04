class Solution1:
    def numDecodings(self, s: str) -> int:


        self.ans = 0
        if len(s) == 0:
            return self.ans

        def numberDecode(string,cur):
            if cur == len(string):
                self.ans += 1
                return
            if cur > len(string):
                return

            if string[cur] > '0' and string[cur] <= '9':
                numberDecode(string,cur+1)
            if string[cur:cur+2] >= '10' and string[cur:cur+2] <= '26':
                numberDecode(string,cur+2)

        numberDecode(s,0)
        print(self.ans)


class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2,len(s)+1):
            oneDig = s[i-1:i]
            twoDig = s[i-2:i]

            if oneDig >= '1':
                dp[i] += dp[i-1]
            if twoDig >= '10' and twoDig <= '26':
                dp[i] += dp[i-2]

        return dp[len(s)]

Solution().numDecodings("111111111111111111111111111")