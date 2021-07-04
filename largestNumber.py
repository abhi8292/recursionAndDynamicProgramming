

def findLaregestNumber(nums):
    max = nums[0]
    for i in range(1,len(nums)):
        if max+nums[i] > nums[i]+max:
            max = max+nums[i]
        else:
            max = nums[i] + max
    print(max)


inp = ['17','3','30','91','9']

# findLaregestNumber(inp)
inp.sort(reverse=True)
findLaregestNumber(inp)
