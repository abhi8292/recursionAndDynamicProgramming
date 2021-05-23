class Solution:
    def lastStoneWeight(self, stones) -> int:

        global diff
        while (len(stones) > 1):
            stones.sort(reverse=True)
            # print(stones)
            diff = abs(stones[0] - stones[1])
            # print(diff,stones[0],stones[1])

            if diff == 0:
                stones = stones[2:]
            else:
                stones = stones[2:]
                stones.append(diff)
        if stones:
            print(stones[0])
        else:
            print(diff)


inp = [2,7,4,1,8,1]
Solution().lastStoneWeight(inp)
