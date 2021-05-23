import random
nums=[]
for i in range(0,10):
    nums.append(random.randint(2,99))
def sortFunc(nums):
    size = len(nums)
    if size >1:
        mid = size //2
        left = nums[:mid]
        right = nums[mid:]

        sortFunc(left)
        sortFunc(right)

        i = 0
        j = 0
        k = 0
        while i<len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i +=1
            else:
                nums[k] = right[j]
                j +=1
            k +=1

        while i < len(left):
            nums[k] = left[i]
            k +=1
            i +=1
        while j < len(right):
            nums[k] = right[j]
            k +=1
            j +=1



print("Before Sorting =>>>>>>>>>",nums)
sortFunc(nums)
print("After sorting  =>>>>>>>>>",nums)