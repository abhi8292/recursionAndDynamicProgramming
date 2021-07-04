class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        nums.sort()
        ans = set()
        size = len(nums)
        for i in range(0, size - 3):
            for j in range(i + 1, size - 2):

                left = j + 1
                right = size - 1

                while left < right:

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    elif total == target:
                        temp = str(nums[i]) + ',' + str(nums[j]) + ',' + str(nums[left]) + ',' + str(nums[right])
                        ans.add(temp)
                        right -= 1
                        left += 1
        result = []

        for i in ans:
            result.append(i.split(','))
        return result


inp = [0,0,0,0]
target = 0
print(Solution().fourSum(inp,target))