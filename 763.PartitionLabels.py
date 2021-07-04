class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        dicStr = {}
        for i in range(0,len(s)):
            if s[i] in dicStr.keys():
                dicStr[s[i]] = max(i,dicStr[s[i]])
            else:
                dicStr[s[i]] = i
        self.ans =[]
        j = 0
        count = 0
        for i in range(0,len(s)):
            a = s[i]
            b = j
            if i > j:
                self.ans.append(count)
                count = 0
            count += 1
            j = max(j,dicStr[s[i]])
        self.ans.append(count)
        return self.ans

# inp = "ababcbacadefegdehijhklij"
inp = "ababcbacadefegdehijhklijsfsafsagsagafsafsafasfsazzxxzxxzxzx"
Solution().partitionLabels(inp)