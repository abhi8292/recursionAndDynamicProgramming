import sys


# class Solution:
#     def minSubArrayLen(self, target: int, nums: list[int]) -> int:
#
#         ans = sys.maxsize
#         n = len(nums)
#         left = 0
#         sum1 = 0
#
#         for i in range(0, n - 1):
#
#             sum1 += nums[1];
#
#             while sum1 >= target:
#                 ans = min(ans, i + 1 - left)
#                 left = left + 1
#                 sum1 = sum1 - nums[left]
#
#         if ans != sys.maxsize:
#             return ans
#         else:
#             return 0

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        lb = 0
        ub = 0
        wSum = nums[0]
        numLen = len(nums)
        ans = []
        while lb < numLen:
            # print(lb, ub, wSum)
            if wSum >= target:
                ans.append(ub - lb + 1)

            if wSum < target and ub + 1 < numLen:
                ub += 1
                wSum += nums[ub]
            else:
                wSum -= nums[lb]
                lb += 1

        # print(ans)
        if ans:
            return min(ans)
        return 0

inp = [2,3,1,2,4,3]
target = 7

Solution().minSubArrayLen(target,inp)