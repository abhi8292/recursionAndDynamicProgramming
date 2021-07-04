graph = {
            1:[5,2],
            2:[50,1],
            50:[6,2],
            5:[12,7,1],
            12:[],
            7:[10,8,5],
            10:[],
            8:[]
        }

def findKdistanceNodeDFS(src,dis,graph,lvl,seen,ans):

    for i in src:
        if i not in seen:
            if lvl == dis:
                ans.append(i)
            else:
                seen.add(i)
                findKdistanceNodeDFS(graph[i],dis,graph,lvl+1,seen,ans)



def findNodeBFS(visited,dis,lvl,seen):
    temp =[]
    for i in visited:
        if i not in seen:
            for j in graph[i]:
                if j not in seen:
                    temp.append(j)
                    # seen.add(j)
            seen.add(i)
    lvl += 1
    if dis == lvl:
        return temp
    return findNodeBFS(temp,dis,lvl,seen)


src = [5]
dis = 4
ans =[]
findKdistanceNodeDFS(src,dis,graph,0,set(),ans)
print(ans)
seen = set()
# seen.add(src[0])
print(findNodeBFS(src,dis,0,seen))