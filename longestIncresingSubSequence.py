
def longesIncresingSubSeq(nums,ind,cur):
    global ans
    if ind == len(nums):
        ans.append(cur.copy())
        return

    for i in range(ind,len(nums)):


        if nums[i] > cur[len(cur)-1]:
            cur.append(nums[i])
            longesIncresingSubSeq(nums,i+1,cur)
        cur.pop()


inp = [5,8,7,1,9]
ans = []
longesIncresingSubSeq(inp,1,[5])
print(ans)