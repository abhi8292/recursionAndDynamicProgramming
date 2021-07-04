class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a) - 1
        j = len(b) - 1
        ans = list()
        carry = 0

        while i >= 0 or j >= 0:

            sumNum = carry
            if i >= 0:
                sumNum += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                sumNum += ord(b[j]) - ord('0')
                j -= 1

            ans.insert(0,str(sumNum%2))
            carry = sumNum // 2
        if carry >0:
            ans.insert(0,'1')
        print("".join(ans))

Solution().addBinary('111','111')
