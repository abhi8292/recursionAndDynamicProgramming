def perm(list):

    ans = []
    def helper(list,ind,cur):

        if ind == len(list):
            ans.append(cur)
            return

        helper(list,ind+1,cur)
        helper(list,ind+1,cur+[list[ind]])

    helper(list,0,[])
    print(ans,len(ans))


li = [1,2,3,4]
perm(li)