class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], num_wanted: int, use_limit: int) -> int:

        labValDic = {}
        items = []
        ans = 0

        for i in range(len(labels)):
            items.append(Item(values[i], labels[i], i))
            if labels[i] in labValDic.keys():
                labValDic[labels[i]].append(values[i])
            else:
                labValDic[labels[i]] = [values[i]]
        print(labValDic)

        items = sorted(items, key=lambda i: i.value)

        labDic = {}
        for i in labels:
            if i not in labDic.keys():
                labDic[i] = 0

        while items and num_wanted > 0:

            cur = items.pop()
            if labDic[labels[cur.index]] >= use_limit:
                continue
            else:
                ans += cur.value
                labDic[labels[cur.index]] += 1
                num_wanted -= 1
        print(ans)


class Item:

    def __init__(self, value, label, index):
        self.value = value
        self.label = label
        self.index = index


Solution().largestValsFromLabels([9,8,8,7,6],[0,0,0,1,1],3,2)