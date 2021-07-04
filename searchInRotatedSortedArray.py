
def searchItem(num,target):
    left = 0
    right = len(num)

    while left<right:
        mid = (left+right) // 2

        if num[mid] == target:
            return mid
        if num[mid] < target:
            left = mid +1
        else:
            right = mid
    return -1

def findElement(nums,target):
    print(nums,target)
    left = 0
    right = len(nums)-1
    pivot= None

    while left < right:
        mid = (left+right) // 2

        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            pivot = nums[mid]
            break
        if nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid

    print(pivot ,mid)
    if target == pivot:
        return mid
    ans = None

    if target >= nums[0] and target < mid:
        ans = searchItem(nums[:mid+1],target)

    else:
        ans = searchItem(nums[mid:],target)
        if ans != -1:
            ans = ans + mid

    print(ans)

    if nums[ans] == target:
        print('Passed')
    else:
        print('Failed')

inp = [4,5,6,7,8,9,15,19,21,0,1,2,3]
# arr = [4,5,6,7,8,9,15,19,21]
target = 0

findElement(inp,target)

# print(searchItem(arr,target))