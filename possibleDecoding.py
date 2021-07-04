def decodeHelpe(s, n):

    if n == 0 or n == 1:
        return 1
    count = 0
    if s[n-1] >'0':
        count = decodeHelpe(s,n-1)
    if s[n-2] == '1' or s[n-2] == '2' and s[n-1] < '7':
        count += decodeHelpe(s,n-2)

    return count



def numDecoding(s:str()):

    if len(s) ==0 or len(s) == 1 and s[0] == '0':
        return 0
    return decodeHelpe(s,len(s))
    # return s


n = '1214'

print(numDecoding(n))