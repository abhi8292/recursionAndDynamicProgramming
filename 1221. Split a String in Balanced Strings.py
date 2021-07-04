class Solution:
    def balancedStringSplit(self, s: str) -> int:

        self.ans = 0
        arr= [0] * 2

        if s[0] == 'R':
            arr[1] = 1
        else:
            arr[0] = 1
        j = 1
        while j < len(s):
            if arr[0] == arr[1] and arr[0] > 0:
                self.ans += 1
                arr =[0]*2

            if s[j] == 'R':
                arr[1] += 1
            else:
                arr[0] += 1
            j += 1

        if arr[0] == arr[1] and arr[0] > 0:
            self.ans += 1
        print(self.ans)


inp = "RLRRRLLRLLLR"

Solution().balancedStringSplit(inp)