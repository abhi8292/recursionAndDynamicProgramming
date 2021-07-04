class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        self.ans = False

        def canSum(targetSum, numbers, memo={},ind=0):
            if targetSum in memo.keys():
                return memo[targetSum]
            if targetSum == 0:
                return True
            if targetSum < 0:
                return False
            for num in range(ind,len(numbers)):
                remain = targetSum - numbers[num]
                if canSum(remain, numbers, memo,num+1):
                    memo[targetSum] = True
                    return True
            memo[targetSum] = False
            return False
        return canSum(target, nums, {},0)

# class Solution:
#     def canPartition(self, nums: list[int]) -> bool:
#
#         total = sum(nums)
#
#         if total % 2 != 0:
#             return False
#
#         target = total // 2
#         self.ans = False
#
#         def findTarget(nums, target, cur):
#
#             if target == 0:
#                 # self.ans = True
#                 return True
#             for i in range(cur, len(nums)):
#                 findTarget(nums, target - nums[i], i + 1)
#
#         if findTarget(nums, target, 0):
#             return True
#         else:
#             return False
#         # return self.ans

inp =[100,100,99,97]
print(Solution().canPartition(inp))