


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.count = 0
        self.ans = set()
        self.size = len(tiles)

        def countTile(tiles,cur):

            if cur:
                self.ans.add("".join(cur))
            if len(tiles) == 0:
                return

            for i in range(0,len(tiles)):
                cur = cur + [tiles[i]]
                countTile(tiles[:i]+tiles[i+1:],cur)
                cur.pop()






        countTile(tiles,[])
        print(self.ans,len(self.ans))




inp = 'AAABBC'
Solution().numTilePossibilities(inp)