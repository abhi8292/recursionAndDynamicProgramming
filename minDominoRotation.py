class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:

        def minSwap(target,a,b):
            cont = 0
            size = len(a)
            for i in range(0,size):
                if a[i] != target and b[i] != target:
                    return size
                elif a[i] != target:
                    cont += 1
            return cont
        ans = min(minSwap(tops[0],tops,bottoms),minSwap(bottoms[0],tops,bottoms),minSwap(tops[0],bottoms,tops),minSwap(bottoms[0],bottoms,tops))
        if ans == len(tops):
            return -1
        else:
            return ans

tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
Solution().minDominoRotations(tops,bottoms)