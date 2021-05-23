class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        def binarySearch(item, target):
            st = 0
            end = len(item)

            while st < end:

                mid = (st + end) // 2
                if item[mid] == target:
                    return True
                if item[mid] > target:
                    end = mid
                else:
                    st = mid + 1
            return False

        print(binarySearch([2, 5, 8, 12, 19], 5))



inp =[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
Solution().searchMatrix(inp,target)