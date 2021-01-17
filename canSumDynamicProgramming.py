'''
Write a function canSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments.
The function should return a boolean indicating whether or not it is possible to generate the targetSum using
numbers from the array.

you may use an element of the array as many times as needed
you may assume that all input numbers are non-negative.
canSum(7,[5,3,4,7]) => True
canSum(7,[2,4])  => False
'''


def canSum(targetSum, numbers, memo={}):
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        remain = targetSum - num
        # print(remain, numbers, canSum(remain, numbers))
        if canSum(remain, numbers, memo):
            memo[targetSum] = True
            return True
            # return memo[targetSum]
    memo[targetSum] = False
    return False
    # return memo[targetSum]


print(canSum(7, [2, 3] , {}))  # Expected Output => True
print(canSum(7, [5, 3, 4, 7],{}))  # Expected Output => True
print(canSum(7, [2, 4],{}))  # Expected Output => False
print(canSum(8, [2, 3, 5],{}))  # Expected Output => True
print(canSum(300, [7, 14],{}))  # Expected Output => False
