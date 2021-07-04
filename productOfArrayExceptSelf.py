def findProductExceptSelf(nums):
    print(nums)
    leftProduct=[0] * len(nums)
    rightProdut =[0] * len(nums)
    leftProduct[0] =nums[0]
    for i in range(1,len(nums)):
        leftProduct[i] = leftProduct[i-1] * nums[i]
    print(leftProduct)

    rightProdut[len(nums)-1] = nums[len(nums)-1]
    for i in range(len(nums)-2,-1,-1):
        rightProdut[i] = rightProdut[i+1] * nums[i]

    print(rightProdut)

    result =[0] * len(nums)

    result[0] = rightProdut[1]
    result[len(nums)-1] = leftProduct[len(nums)-2]
    for i in range(1,len(nums)-1):
        result[i] = leftProduct[i-1] * rightProdut[i+1]

    print(result)



inp = [2,2,3,4]

findProductExceptSelf(inp)