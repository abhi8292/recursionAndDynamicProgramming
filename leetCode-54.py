class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        size = len(matrix) * len(matrix[0])
        print(size)

        start = 0
        top = 0
        right = len(matrix[0])
        bottom = len(matrix) - 1
        left = len(matrix) - 1

        while len(ans) < size:
            pass


inp = [[1,2,3],[4,5,6],[7,8,9]]
Solution().spiralOrder(inp)
