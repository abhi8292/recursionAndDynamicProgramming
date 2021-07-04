class Solution:
    def compress(self, chars: list[str]) -> int:
        count = 1
        j = 0
        global cur
        cur = ""
        for i in range(1,len(chars)):
            cur = chars[i]
            src = chars[i]
            tar = chars[i-1]
            if src == tar:
                count += 1
            else:
                if count > 1 and count < 10:
                    chars[j] = chars[i-1]
                    j += 1
                    chars[j] = count
                    j += 1
                if count > 9:
                    for k in str(count):
                        chars[j] = k
                        j += 1
                # j = i + 1
                if count == 1:
                    chars[j] = chars[i-1]
                    j += 1
                count = 1
        if cur != chars[j-2]:
            chars[j] = chars[i-1]
        j += 1
        if count > 1 and count < 10:
            chars[j] = chars[i - 1]
            j += 1
            chars[j] = count
            j += 1
        if count > 9:
            for k in str(count):
                chars[j] = k
                j += 1
        print(j)
        print(chars)

# inp = ["a","a","b","b","c","c","c"]
# inp =["a","b","b","b","b","b","b","b","b","b","b","b","b"]
inp = ["a","a","a","b","b","a","a"]
# inp =["a"]
Solution().compress(inp)