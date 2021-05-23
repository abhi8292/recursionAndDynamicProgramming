
ans = 0
def noOfForm(N,cur,val):
    global ans
    if val < 0:
        return None
    if val == 0:
        return True
    for i in range(N):
        ans1 = noOfForm(N,cur,val-cur[i])
        if ans1 == True:
            ans = ans + 1


N = int(input())
cur = []

for i in range(N):
    cur.append(int(input()))

val = int(input())
noOfForm(N,cur,val)
print(ans)