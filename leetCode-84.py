class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        lar = 0

        for i in range(0, len(heights) - 1):

            for j in range(i + 1, len(heights)):
                temp = (j - i + 1) * min(heights[i:j+1])
                lar = max(lar, temp)

        print(lar)

inp = [2,1,5,6,2,3]
Solution().largestRectangleArea(inp)