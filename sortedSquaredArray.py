
def sortArray(nums):

    size = len(nums)
    if size >1:

        mid = size // 2

        left = nums[:mid]
        right = nums[mid:]

        sortArray(left)
        sortArray(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

            if abs(left[i]) < abs(right[j]):
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):

            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

'''
Time Complexity  = O(NlogN)
'''

def sortedSquareArray(nums):
    print(nums)
    sortArray(nums)
    print(nums)

    for i in range(0,len(nums)):

        nums[i] = nums[i] * nums[i]

    print(nums)


'''
Time Complexity = O(N)
'''
def sortedSquareArrayN(nums):
    i = 0
    j = len(nums) -1
    ouput = [0] * (j+1)

    count = j
    while count < 0:

        if abs(nums[i]) > abs(nums[j]):
            ouput[count] = nums[i] * nums[i]
        else:
            ouput[count] = nums[j] * nums[j]
        count -= 1

    print(nums)


inp = [-7,-3,-1,4,8,12]
# inp = [-3,-2,-1]
sortedSquareArray(inp)
sortedSquareArrayN(inp)